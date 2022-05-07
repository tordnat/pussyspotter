from lib2to3.pgen2 import token
import os
from slackeventsapi import SlackEventAdapter
from slack_sdk.web import WebClient
from flask import Flask

slack_signing_secret = "2be2e32989fa5f57c46d7971f974e2df" #os.environ['SLACK_SIGNING_SECRET']
slack_app_token = 'xoxb-235646072290-3363750293190-ci8s7zFX9W9EJYoDy9SXcyhL' #os.environ['SLACK_TOKEN']

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(slack_signing_secret,'/slack/events',app)
web_client = WebClient(token=slack_app_token)

bot_id = None
startup_message="Hello my pussylovers!"
def slack_print_channel(text):
    web_client.chat_postMessage(channel="#pussy_testing", text=text)

@slack_event_adapter.on('message')
def mention(POST):
    global bot_id
    event = POST.get('event', {})
    user_id = event.get('user')
    message_text = event.get('text')
    if bot_id is None and message_text == startup_message: #Startup
        bot_id = user_id
        print(f"Bot ID :{str(bot_id)}")
    ## Filter
    if user_id != bot_id:
        slack_print_channel(f"Ur mom {message_text.strip('ur')}")

def get_slack_images(POST):
    headers = f"Authorization: Bearer {slack_app_token}"
    for file_obj in POST.get('files'):
        for image in file_obj.get()

        
    
    #web_client.chat_postMessage(channel="#pussy_testing", text=slack_print_channel(text))

# Startup
if __name__ == "__main__":
    web_client.chat_postMessage(channel="#pussy_testing", text=startup_message)
    app.run(debug=False)