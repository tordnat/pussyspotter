#!/bin/sh
cd darknet
make
wget https://pjreddie.com/media/files/yolov3.weights
./darknet detect cfg/yolov3.cfg yolov3.weights ../pussydata/test1.jpg
printf "Done! Check prediction.jpg in the /darknet directory for benchmark \n"
