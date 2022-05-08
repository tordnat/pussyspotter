## Program to run darkned classification on incoming pussy
## and archiving both the prediciton and origional
## Both archived and predicted will be time-stamped to avoid
## name conflicts

## Logging
import logging
verbose_logger = True

from datetime import datetime
import os
from os.path import dirname, abspath
import subprocess

## Environment variables, there can only be one boilerplate
output_buffer_file = os.getenv("YOLO_STOUT_BUFFER")
formatted_buffer_file = os.getenv("YOLO_FORMATTED_STOUT_BUFFER")

## FIX: Something funky here!!!! Should load in envfiles correctly
def format_buffer_output(): #I fucking hate this
    output_buffer_file = os.getenv("YOLO_STOUT_BUFFER")
    formatted_buffer_file = os.getenv("YOLO_FORMATTED_STOUT_BUFFER")
    input_file = open(output_buffer_file)
    output_file = open(formatted_buffer_file, 'w')
    output_file.truncate(0)
    input_file = input_file.read().split("\n")
    foo = input_file[0]
    foo = foo.split(" ")
    foo.pop(0)
    foo = ' '.join(foo)
    output_file.write(str(foo))
    #input_file.pop(0)
    for i in range(1,len(input_file)):
        output_file.write('\n' + input_file[i])

#### File formatting and logging
def file_format_filter(file : str):
    return file.endswith(".jpg") or file.endswith(".png")

def is_valid_file(file : str):
    foo = file_format_filter(file)
    if(foo):
        return True
    else:
        print("Invalid file format")
        return False

## Loggers
def print_predictions():
    file = open(formatted_buffer_file, 'r')
    for i in file:
        print(i)

### Searching for cats in detections
def cat_log_search():
    file = open(formatted_buffer_file, 'r')
    file = file.read()
    cat = file.find("cat")
    if(cat != -1):
        print("Pussy detected!")
        if(verbose_logger): print_predictions()
        return True
    return False

## TO-DO: implement threshold for some reason
def prediction(file : str, threshold : float):
    if (is_valid_file(file)):
        subprocess.run(["scripts/yolo_predict.sh", file])
        format_buffer_output()
        return True
    else:
        return False

def pussy_detector(file : str, threshold = 1.0): #Dependent on the current buffer being the latest
    try:
        env_path = dirname(abspath(".")+"/config"+"/env.sh")
        load_dotenv(env_path)
        print(f"Loaded filepath: {file}")
        prediction(file, threshold)
        print("Prediction done!")
        return cat_log_search()
    except:
        print("Ouuups something went wrong")
        return 1

