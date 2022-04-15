#!/bin/sh
if [ "$1" ]; then
  echo 'Image loaded: '$1
else
  echo 'Missing image' 
  exit
fi
PATH=${PWD}
cd  $PATH/darknet
$DARKNET_PATH/darknet detect $YOLO_CONFIG $YOLO_WEIGHTS $PATH/$1 > $YOLO_STOUT_BUFFER
