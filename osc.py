from pythonosc import osc_message_builder
from pythonosc import udp_client
import time
import argparse

def setupOSC(port):
    # Defining OSC Client
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=port,help="The port the OSC server is listening on") # this is the port we are sending to
    args = parser.parse_args()
    client = udp_client.SimpleUDPClient(args.ip, args.port)
    return [client,port]

def sendOSC(client,periodTime,df,port):
    # Send OSC messages, wait periodTime between each message
    print("OSC sender started, sending to port ", port)
    for x in range(0, len(df)):
        lefthand= df.iloc[x]['LHandMaxPosY']
        print(lefthand)
        client.send_message("/LHandMaxPosY", lefthand)
        time.sleep(periodTime)