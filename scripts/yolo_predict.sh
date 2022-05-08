#!/bin/bash
if [ "$1" ]; then
  echo 'Image loaded: '$1
else
  echo 'Missing image' 
  exit
fi
source ./config/env.sh
cd $DARKNET_PATH
$DARKNET_PATH/darknet detect $YOLO_CONFIG $YOLO_WEIGHTS $1
