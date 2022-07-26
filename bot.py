import logging
import os
from os.path import dirname, abspath
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import requests
import re
from predict import pussy_detector
from dotenv import load_dotenv

## Loading .env
load_dotenv()

#Shitty globals
accepted_filetypes = ("jpg", "png", "JPG", "PNG")
slack_bot_token = os.getenv("SLACK_BOT_TOKEN")
pussy_archive_filepath = os.getenv("PUSSY_ARCHIVE_PATH")

app = App()

@app.event("app_mention")
def event_test(body, say, logger):
    logger.info(body)
    event = body["event"]
    thread_ts = event.get("thread_ts", None) or event["ts"]
    file=get_slack_images(body=event, say=say, thread_ts=thread_ts)
    if file: #If file, run detector and upload result to thread
        result = pussy_detector(file)
        say(f'{result}', thread_ts=thread_ts)
        upload_result(thread_ts=thread_ts, channel=event.get("channel"))

def get_slack_images(body, say, thread_ts):
    files = body.get('files')
    if files is None: #Filter for files
        return None
    else:
        for file_obj in files:
            if file_obj.get('filetype') in accepted_filetypes: #Filtering for images             
                say(f"Archiving file: {file_obj.get('name')}", thread_ts=thread_ts)
                filepath = get_file_from_url(file_obj.get('url_private_download'))
                say(f"File saved as {filepath}", thread_ts=thread_ts)
                return filepath
        return say(f"Error: Unsupported file format", thread_ts=thread_ts)
                
def upload_result(thread_ts, channel):
    return app.client.files_upload(file="darknet/predictions.jpg", channels=channel, title="Predictions", thread_ts=thread_ts)

def get_file_from_url(url):
    resp = requests.get(url, headers={'Authorization': 'Bearer %s' % slack_bot_token})
    headers = resp.headers['content-disposition']
    fname = re.findall("filename=(.*?);", headers)[0].strip("'").strip('"')
    assert not os.path.exists(fname), print("File already exists. Please remove/rename and re-run")
    file_path = pussy_archive_filepath+fname
    out_file = open(file_path, mode="wb+")
    out_file.write(resp.content)
    out_file.close()
    return file_path

if __name__ == "__main__":
    app.start(3000)