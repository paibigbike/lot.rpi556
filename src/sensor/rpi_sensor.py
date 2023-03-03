# Copyright (C) 2023 Chatpon Chaimongkol <chatponc65@nu.ac.th>

"""



"""

__author__ = "Chatpon Chaimongkol"


# standard library
from datetime import datetime as dt
import json
import time

# installed library
import paho.mqtt.client as mqtt
from gpiozero import CPUTemperature

# local files
from config import *

client = mqtt.Client()
client.connect(HIVEMQTT_BROKER, HIVEMQTT_PORT)
client.loop_start()


while True:
    # send a massage to MQTT server
    payload = {"datetime": dt.now().strftime("%Y-%m-%d %H:%M:%S"),
               "device": "device Chatpon",
               "temperature": temperature}
    temperature = (temperature+1) % 10
    print(f"payload: {payload}")
    client.publish(PUBLISH_DATA_TOPIC, json.dumps(payload))
    # sleep foe 15 second
    time.sleep(15)