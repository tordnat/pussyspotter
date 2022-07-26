#!/bin/bash
if [ "$1" ]; then
  echo 'Image loaded: '$1
else
  echo 'Missing image' 
  exit
fi
source .env
cd $DARKNET_PATH
rm log.txt
$DARKNET_PATH/darknet detect $YOLO_CONFIG $YOLO_WEIGHTS $1 | tee -a log.txt
