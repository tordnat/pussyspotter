## Program to run darkned classification on incoming pussy

from datetime import datetime
import os
from os.path import dirname, abspath
import subprocess

### Searching for cats in detections
def cat_log_search():
    darknet_log = open("darknet/log.txt", 'r').readlines()[1:] #Ignore first line
    for line in darknet_log:
        if line.find("cat") != -1:
            return line

def prediction(file : str):
    subprocess.run(["scripts/yolo_predict.sh", file])

def pussy_detector(file : str): #Dependent on the current buffer being the latest
    print(f"Loaded filepath: {file}")
    prediction(file)
    print("Prediction done!")
    return cat_log_search()