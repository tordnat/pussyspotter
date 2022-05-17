from lib2to3.pgen2 import token
import os
from os.path import dirname, abspath
import shutil
import re
import requests
from urllib import response
from slackeventsapi import SlackEventAdapter
from slack_sdk.web import WebClient
from flask import Flask
from pathlib import Path
from dotenv import load_dotenv
from predict import pussy_detector
import time

## Load environment variables
env_path = dirname(abspath(".")+"/config"+"/env.sh")
load_dotenv(env_path)

#temp boilerplate
slack_signing_secret = "redacted" #os.getenv('SLACK_SIGNING_SECRET')
slack_app_token = 'redacted' #os.getenv('SLACK_TOKEN')
pussy_archive_filepath = "pussydata/pussy_archive/"

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(slack_signing_secret,'/slack/events',app)
web_client = WebClient(token=slack_app_token)

bot_id = None
startup_message="Hello my pussylovers!"
accepted_filetypes = ("jpg", "png", "JPG", "PNG")

def slack_print_channel(text):
    web_client.chat_postMessage(channel="#pussy_testing", text=text)

def slack_print_thread(text, ts):
    web_client.chat_postMessage(channel='#pussy_testing', text=text, thread_ts=ts)

@slack_event_adapter.on('message')
def message(POST):
    global bot_id
    event = POST.get('event', {})
    user_id = event.get('user')
    message_text = event.get('text')
    message_thread = event.get('ts')
    subtype = event.get("subtype")
    print(f"Thread: {message_thread}")
    if bot_id is None and message_text == startup_message: #Startup
        bot_id = user_id
        print(f"Bot ID :{str(bot_id)}")
    ## Filter
    if subtype != "bot_message" or user_id==bot_id:  
        filepath = get_slack_images(event, message_thread)
        if filepath != -1:
            resp = pussy_detector(filepath)
            slack_print_thread(text=resp, ts=message_thread)
        

def get_slack_images(POST, ts=None):
    files = POST.get('files')
    if files is None: #Filter for files
        return -1
    else:
        for file_obj in files:
            if file_obj.get('filetype') in accepted_filetypes: #Filtering for images             
                slack_print_thread(f"Archiving file: {file_obj.get('name')}", ts=ts)
                filepath = get_file_from_url(file_obj.get('url_private_download'))
                slack_print_thread(text=f"File saved as {filepath}", ts=ts)
                return filepath


def get_file_from_url(url):
    resp = requests.get(url, headers={'Authorization': 'Bearer %s' % slack_app_token})
    headers = resp.headers['content-disposition']
    fname = re.findall("filename=(.*?);", headers)[0].strip("'").strip('"')
    assert not os.path.exists(fname), print("File already exists. Please remove/rename and re-run")
    file_path = pussy_archive_filepath+fname
    out_file = open(file_path, mode="wb+")
    out_file.write(resp.content)
    out_file.close()
    return abspath(".")+"/" + file_path
        
    
#web_client.chat_postMessage(channel="#pussy_testing", text=slack_print_channel(text))

# Startup
if __name__ == "__main__":
    web_client.chat_postMessage(channel="#pussy_testing", text=startup_message)
    app.run(debug=True)