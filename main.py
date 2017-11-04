import cv2
import numpy
import math
import pandas as pd
import random


import playVideo
from osc import setupOSC, sendOSC


def readCSV(fileName):
    print("Reading the following file: ", fileName)
    df = pd.read_csv(fileName, sep=",")
    print(df.columns)
    return df

if __name__ == "__main__":
    # set up client for sending OSC messages
    oscClient = setupOSC(5005)[0]
    oscPort= setupOSC(5005)[1]
    periodTime=1/120
    dataFrame = readCSV("/Users/emmafrid/Desktop/SONAO/Code/FormatMocapData_Python/data_formatted/sadness_clip-0048.csv")

    # send OSC messages at 120 Hz
    sendOSC(oscClient,periodTime,dataFrame,oscPort)
    # play video
    playVideo("/Users/emmafrid/Box Sync/SONAODM2350-Files/EvaluationOfAnimations/Sad_Joyful/sad_clip-048.sub_level1.mp4")
