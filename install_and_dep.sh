#!/bin/sh
virtualenv -q pussyspotter_env
pussyspotter_env/bin/pip install -r requirements.txt
export SLACK_BOT_TOKEN='--'
python main.py
