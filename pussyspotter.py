## Program to run darkned classification on incoming pussy
## and archiving both the prediciton and origional
## Both archived and predicted will be time-stamped to avoid
## name conflicts
import sys
import logging
from datetime import datetime
import os

## Boilerplate path
archive_path = "./pussydata/pussy_archive/"
prediction_path = "./pussydata/pussy_predictions/"

def prectiction(filename : str, threshold : float):


def timestamp_filename(filename : str):
    filename = str(datetime.now()) + filename
    return filename
