#!/bin/sh
if [ "$1" ]; then
  echo 'Good boi for sending args: '$1
else
  echo 'Missing image path' 
  exit
fi

FILE="pussyspotter_"$1

cp $YOLO_PREDICTION_IMAGE $PUSSY_PREDICTION_PATH/$FILE

