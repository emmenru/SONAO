from pythonosc import osc_message_builder
from pythonosc import udp_client
import time


SEND_TIME_CONSTANT = 0.00022063018433281004
def setupOSC(port):
    # Defining OSC Client
    client = udp_client.SimpleUDPClient("127.0.0.1", port)
    return client, port


def sendOSC(client, periodTime, left_data, port):
    # Send OSC messages, wait periodTime between each message
    print("OSC sender started, sending to port ", port)
    start = time.time()
    
    for x in range(0, len(left_data)):
        client.send_message("/LHandMaxPosY", left_data[x])
        time.sleep(periodTime-SEND_TIME_CONSTANT)
    end = time.time()
    print('done. time={}s'.format(end-start))

