## Program to run darkned classification on incoming pussy
## and archiving both the prediciton and origional
## Both archived and predicted will be time-stamped to avoid
## name conflicts
import sys

# Log every detection
import logging
from datetime import datetime
import os
import subprocess

output_buffer_file = os.environ["YOLO_STOUT_BUFFER"]
formatted_buffer_file = os.environ["YOLO_FORMATTED_STOUT_BUFFER"]

def timestamp_filename(filename : str):
    filename = str(datetime.now()) + filename
    return filename

def format_buffer_output(): #I fucking hate this
    input_file = open(output_buffer_file)
    output_file = open(formatted_buffer_file, 'w')
    output_file.truncate(0)
    input_file = input_file.read().split("\n")
    foo = input_file[0]
    foo = foo.split(" ")
    foo.pop(0)
    foo = ' '.join(foo)
    output_file.write(str(foo))
    input_file.pop(0)
    for i in range(1,len(input_file)):
        output_file.write('\n' + input_file[i])

# TO-DO: ffmpeg unsupported formats to jpg
#def ffmpeg(file : str):


#### File formatting
def file_format_filter(file : str):
    return file.endswith(".jpg")

def is_valid_file(file : str):
    foo = file_format_filter(file)
    if(foo):
        return True
    else:
        print("Invalid file format")
        return False
def prediction(file : str, threshold : float):
    if (is_valid_file(file)):
        subprocess.run(["scripts/yolo_predict.sh", file])
        format_buffer_output()
        return True
    else:
        return False

### Searching for cats in detections
def cat_log_search():
    file = open(formatted_buffer_file, 'r')
    file = file.read()
    cat = file.find("cat")
    if(cat):
        print("Cat detected in logs")
        return True
    return False


def cat_detector(file : str, threshold = 1.0): #Dependent on the current buffer being the latest
    try:
        prediction(file, threshold)
        return cat_log_search()
    except:
        print("Ouuups something went wrong")
        return 1


cat_detector("pussydata/test1.jpg")
