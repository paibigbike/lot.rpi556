# Copyright (C) 2023 Chatpon Chaimongkol <chatponc65@nu.ac.th>

"""

Make a script that will read a number from the HIVE MQTT on the topic "Naresuan/Final/{Name}/Rx"
and square that number and send it to the topic "Naresuan/Final/{Name}/Tx"

"""

__author__ = "Chatpon Chaimongkol"

import paho.mqtt.client as mqtt

# MQTT Broker information
broker_address = "broker.hivemq.com"
broker_port = 8000
keepalive = 60

# MQTT Topic information
name = "Chatpon"
rx_topic = f"Naresuan/Final/Chatpon/Rx"
tx_topic = f"Naresuan/Final/Chatpon/Tx"

# Connect to the MQTT broker
client = mqtt.Client()
client.connect(broker_address, broker_port, keepalive)


def on_connect(client, userdata, flags, rc):
    # Define callback functions
    print("Connected with result code "+str(rc))
    client.subscribe(rx_topic)


def on_message(client, userdata, message):
    # Square the received number and send it to the TX topic
    number = int(message.payload.decode())
    result = number ** 2
    client.publish(tx_topic, str(result))

# Set up callback functions
client.on_connect = on_connect
client.on_message = on_message

# Start the MQTT loop
client.loop_forever()
