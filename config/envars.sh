#!/bin/bash
export PUSSY_ARCHIVE_PATH=${PWD}'/pussydata/pussy_archive'
export PUSSY_PREDICTION_PATH=${PWD}'/pussydata/pussy_predictions'

export DARKNET_PATH=${PWD}'/darknet'
export YOLO_PREDICTION_IMAGE=${PWD}'/darknet/predictions.jpg'
export YOLO_CONFIG=${PWD}'/darknet/cfg/yolov3.cfg'
export YOLO_WEIGHTS=${PWD}'/darknet/yolov3.weights'
export YOLO_DATA=${PWD}'/darknet/cfg/coco.data'
export YOLO_STOUT_BUFFER=${PWD}'/darknet/log.txt'
export YOLO_FORMATTED_STOUT_BUFFER=${PWD}'/pussydata/formatted_buffer.txt'
