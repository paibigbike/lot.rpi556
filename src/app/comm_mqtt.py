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

#local file
import main_qui2



HIVEMQTT_PORT = 1883  # CONSTANT
HIVEMQTT_BROKER = "broker.hivemq.com"
PUBLISH_TOPIC = "Naresuan/Chatpon"
SUBSCRIBE_TOPIC = "Naresuan/+"


class MQTTConn:
    def __init__(self, root: main_qui2.SensorUI):
        self.root = root
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connection
        # self.client.on_subscribe = on_subscription
        self.client.on_message = self.on_massage
        self.client.connect(HIVEMQTT_BROKER, HIVEMQTT_PORT)
        self.client.loop_start()

    def publish(self, massage):
        self.client.publish(PUBLISH_TOPIC, massage)

    # def on_subscription(*args):
        # print("subscribed:", args)

    def on_connection(self, *args):
        """ Call back for when mqtt connect to the broker
        and prints out on acknowleadgement and subsceibes"""
        print("Connected")
        self.client.subscribe(SUBSCRIBE_TOPIC)

    def on_massage(self, client, user_data, msg: mqtt.MQTTMessage):
        print("got massage:", msg.payload)
        print("from topic: ", msg.topic)
        name = msg.topic.split('/')[-1]
        print("massage from:", name)
        if msg.payload == b"on":
            sensor_state = True
        else:
            sensor_state = False

        self.root.change_status(name,
                                sensor_state)


if __name__ == '__main__':
    client = MQTTConn()

    while True:
        client.publish(PUBLISH_TOPIC,
                       "Hello_this is Chatpon")
        time.sleep(5)
