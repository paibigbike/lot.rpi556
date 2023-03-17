# Copyright (C) 2022 Chatpon Chaimongkol <chtponc65@nu.ac.th>

"""
Communicate with the HIVEMQ broker to receive
sensor data, using the paho mqtt library
"""

__author__ = "Chatpon Chaimongkol"

# standard library
from datetime import datetime
import json
import time

# installed library
import paho.mqtt.client as mqtt

# local file
# import main_gui2
from config_final1 import *


class MQTTComm:
    """
    Use the paho library to connect to the HIVE MQ mqtt broker
    Attributes
        root (main_gui.SensorUI): root user interface app
        rooot.data (sensor_data.SensorHubData): master data class for all sensors
        client(mqtt.client): paho client for mqtt communicate
    """

    def __init__(self, root: 'main_gui2.SensorUI'):
        self.root = root
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connection
        # self.client.on_subscribe = on_subscription
        self.client.on_message = self.on_massage
        self.client.connect(HIVEMQTT_BROKER, HIVEMQTT_PORT)
        self.client.loop_start()

    def publish(self, massage, is_data=True):
        """
        Sent a massage to the HIVE MQ broker using the PUBLISH_TOPIC
        Args:
            massage(str): massage to send
        """
        publish_topic = PUBLISH_STATUS_TOPIC
        if is_data:
            publish_topic = PUBLISH_DATA_TOPIC
        self.client.publish(publish_topic, massage)

    # def on_subscription(*args):
    # print("subscribed:", args)

    def on_connection(self, *args):
        """ Call back for when mqtt connect to the broker
        and prints out on acknowledgement and subscribe
        """

        print("Connected")
        self.client.subscribe(SUBSCRIBE_TOPIC)

    def on_massage(self, client, user_data, msg: mqtt.MQTTMessage):
        """
        Callback the receiving massage
        Args:
            client:
            user_data:
            msg(mqtt_MQTTMassage) : massage receiving

        """

        print("got massage:", msg.payload)
        print("from topic: ", msg.topic)
        if len(msg.topic.split('/')) != 3:
            return 201
        sensor = msg.topic.split('/')[1]
        type = msg.topic.split('/')[2]
        print("massage from:", sensor)
        if sensor not in SENSORS_LIST:
            print("Unrecognized sensor, returning")
            return 205  # code error
        if type == "status":
            print("parsing status")
            return self.parse_status_msg(sensor, msg.payload)

        elif type == 'data':
            print("parse data")
            return self.parse_data_msg(msg.payload)
        return 0  # no error

    def parse_data_msg(self, msg):
        print(f"parsing data: {msg} ")
        json_data = json.loads(msg)
        print(f"json data: {json_data}")
        print(f"json_data type: {type(json_data)}")
        if "datetime" not in json_data.keys():
            return 310
        if "device" not in json_data.keys():
            return 311
        if "temperature" not in json_data.keys():
            return 310
        # convert datetime form a string to a datatime object
        date_time = datetime.strptime(json_data["datetime"],
                                      "%Y-%m-%d %H:%M:%S")
        print(f"converted date_time: {date_time}")
        self.root.data.add_data(json_data["device"],
                                date_time,
                                json_data["temperature"])
        return 0

    def parse_status_msg(self, sensor, msg):
        print(f"got msg: {msg} form: {sensor} ")
        if msg == b"on":
            sensor_state = True
        elif msg == b'off':
            sensor_state = False
        else:
            return

        self.root.change_status(sensor,
                                sensor_state)
        return 0


if __name__ == '__main__':
    test_client = MQTTComm()

    while True:
        test_client.publish(PUBLISH_TOPIC,
                            "Hello this is Chatpon")
        time.sleep(5)
