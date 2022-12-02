# Copyright (C) 2022 Chatpon Chaimongkol <catponc65@nu.ac.th>

"""
Communicate with the HIVEMQ broker to recevive
sensor data, using the paho mqtt library
"""

__author__ = "Chatpon Chaimongkol"
# standand library
import time

# installled library
import paho.mqtt.client as mqtt

HIVEMQTT_PORT = 1883 # CONSTANT
HIVEMQTT_BROKER = "broker.hivemq.com"
PUBLISH_TOPIC= "Naresuan/Chatpon"
SUBSCRIBE_TOPIC= "Naresuan/+"

def on_subscription(*args):
    print("subscribed:", args)

def on_connection(*args):
    """ Call back for when mqtt connect to the broker
    and prints out on acknowleadgement and subsceibes"""
    print("Connected")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_massage(client, user_data, msg:mqtt.MQTTMessage):
    print("got massage", msg.payload)


client = mqtt.Client()
client.on_connect = on_connection
client.on_subscribe = on_subscription
client.on_message = on_massage
client.connect(HIVEMQTT_BROKER, HIVEMQTT_PORT)
client.loop_start()
while True:
    client.publish(PUBLISH_TOPIC,
                   "hello_this is Chatpon ")
    time.sleep(5)
