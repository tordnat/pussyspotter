### 
import sys
import logging

from slackeventsapi import SlackEventAdapter
from slack_sdk.web import WebClient
import get_slack_file
import os
import time


def get_random_cat():
    return ""
# Our app's Slack Event Adapter for receiving actions via the Events API
slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events")

# Create a SlackClient for your bot to use for Web API requests
slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
slack_client = WebClient(slack_bot_token)


# Example responder to greetings
@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]
    # If the incoming message contains "hi", then respond with a "Hello" message
    if message.get("subtype") is None and "Pussy plz" in message.get('text'):
        channel = message["channel"]
        message = "Pussy coming up <@%s>! :suscat:" % message["user"]
        pussy = get_random_cat()
        slack_client.chat_postMessage(channel=channel, text=message)
        slack_client.chat_postMessage(channel=channel, text=pussy)

@slack_events_adapter.

# Example reaction emoji echo
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    event = event_data["event"]
    emoji = event["reaction"]
    channel = event["item"]["channel"]
    text = ":%s:" % emoji
    slack_client.chat_postMessage(channel=channel, text=text)


# Error events
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))

# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
slack_events_adapter.start(port=3000)