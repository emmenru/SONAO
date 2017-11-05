import subprocess

import pandas as pd

from video import playVideo
from osc import setupOSC, sendOSC


def readCSV(fileName):
    print("Reading the following file: ", fileName)
    df = pd.read_csv(fileName, sep=",")
    print(df.columns)
    return df


if __name__ == "__main__":
    # play video
    #playVideo("/Users/parham/dev/SONAO/data/sad_clip-048.sub_level1.mp4")

    # set up client for sending OSC messages
    osc_client, osc_port = setupOSC(5005)
    period_time = 0.008303991197183098  # ~1/120
    #period_time = 0.010000
    #period_time = 0.009242957746478873

    data_frame = readCSV("/Users/parham/dev/SONAO/data/sadness_clip-0048.csv")
    left_data = []
    for x in range(0, len(data_frame)):
        left_data.append(data_frame.iloc[x]['LHandMaxPosY'])

    subprocess.run(['open', 'data/sad_clip-048.sub_level1.mp4'])
    # send OSC messages at 120 Hz
    sendOSC(osc_client, period_time, left_data, osc_port)
