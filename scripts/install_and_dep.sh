#!/bin/bash
if [ "$1" ]; then
  echo 'Slack signing secret loaded: '$1
else
  echo 'Missing argument: Slack signing secret' 
  exit
fi
virtualenv -q pussy_env
pussy_env/bin/pip install -r ${PWD}/../requirements.txt
source ${PWD}/../config/envars.sh
export SLACK_SIGNING_SECRET=$1
python ${PWD}/../main.py
