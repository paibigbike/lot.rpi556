# Copyright (C) 2023 Chatpon Chaimongkol <chatponc65@nu.ac.th>

"""

Make a script that will read a number from the HIVE MQTT on the topic "Naresuan/Final/{Name}/Rx"
and square that number and send it to the topic "Naresuan/Final/{Name}/Tx"

"""

__author__ = "Chatpon Chaimongkol"
# installed library
import paho.mqtt.client as mqtt

# local file
import Final_1_gui_Chatpon

HIVEMQTT_PORT = 1883  # CONSTANT
HIVEMQTT_BROKER = "broker.hivemq.com"
PUBLISH_TOPIC = "Naresuan/Chatpon/final"
SUBSCRIBE_TOPIC = "Naresuan/Chatpon/+"
NAME = "Chatpon"

PUBLISH_TOPIC_Tx = "Naresuan/Final/Chatpon/Tx"
SUBSCRIBE_TOPIC_Tx = "Naresuan/Final/Chatpon/+"


class MQTTConn:
    def __init__(self, root: Final_1_gui_Chatpon):

        self.root = root
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connection
        self.client.on_message = self.on_message

        self.client.connect(HIVEMQTT_BROKER, HIVEMQTT_PORT)
        self.client.loop_start()

        self.Pressing = Final_1_gui_Chatpon.Connect_to_Comm

    def publish(self, message):
        """
        Send a message to the HIVE MQ broker using the PUBLISH_TOPIC
        Args:
            message (str): message to send
        """
        self.client.publish(PUBLISH_TOPIC, message)

    def on_connection(self, *args):
        """ Call back for when mqtt connects to the broker
         and prints out an acknowledgement and subscribes """
        print("Connected")
        self.client.subscribe(SUBSCRIBE_TOPIC)
        self.client.subscribe(SUBSCRIBE_TOPIC_Tx)

    def on_message(self, client, user_data, msg: mqtt.MQTTMessage):
        """
            Callback when receiving message
            Args:
            client:
            user_data:
            msg (mqtt.MQTTMessage): message received
        """

        if msg.topic == "Naresuan/Final/Chatpon/Rx":
            msg_tx = int(msg.payload)**2
            self.client.publish(PUBLISH_TOPIC_Tx, msg_tx)

        print("got message: ", msg.payload)
        print("from topic: ", msg.topic)
        name = msg.topic.split('/')[-2]
        print("message from: ", name, '\n')


if __name__ == "__main__":
    test_client = None