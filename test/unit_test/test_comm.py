# Copyright (C) 2023 Chatpon Chaimongkol <chatponc65@nu.ac.th>

"""



"""

__author__ = "Chatpon Chaimongkol"

# standard Libraries
import os
import sys
import unittest
from unittest import mock

# installed library
import paho.mqtt.client as mqtt
sys.path.append(os.path.join("..", "..", "src", "app"))
# local file
import src.app.comm_mqtt as comm_mqtt


class TestComm(unittest.TestCase):
    def test_wrong_sensor(self):
        comm = comm_mqtt.MQTTComm(mock.Mock())
        msg = mqtt.MQTTMessage()
        msg.topic = b"Naresuan/foobar/data"
        return_code = comm.on_massage(None, None, msg)
        print(f"return_code: {return_code}")
        self.assertEqual(return_code, 205)

    def test_on_massage_missing_type(self):
        msg = mqtt.MQTTMessage()
        print(msg)
        msg.topic = b"Naresuan/Chatpon"
        msg.payload = b'{"datetime": "2023-02-08 10:50:18", "device": "device 2", "temperature": 30}'
        comm = comm_mqtt.MQTTComm(mock.Mock())
        return_code = comm.on_massage(None, None, msg)
        print(f"return_code: {return_code}")
        self.assertEqual(return_code, 201)

    def test_on_massage_status_msg(self):
        comm = comm_mqtt.MQTTComm(mock.Mock())
        msg = mqtt.MQTTMessage()
        msg.topic = b"Naresuan/Chatpon/status"
        msg.payload = b'on'
        return_code = comm.on_massage(None, None, msg)
        print(f"return_code: {return_code}")
        self.assertEqual(return_code, 0)
        # check that the self.root.change_status is called
        print(comm.root.change_status.call_args.args)
        print(comm.root.change_status.call_args.call_list)
        print(dir(comm.root.change_status.call_args))
        print(comm.root.change_status)
        print(comm.root)
        # self.assertEqual(comm.root.change_status.call_args.args,
        #                  ("Chatpon", True))
        comm.root.change_status.assert_called_with("Chatpon", True)

    def test_data_rx(self):
        comm = comm_mqtt.MQTTComm(mock.Mock())
        msg = mqtt.MQTTMessage()
        msg.topic = b"Naresuan/Chatpon/data"
        msg.payload = b'{"datetime": "2023-02-08 10:50:18", "device": "device 2", "temperature": 30}'
        return_code = comm.on_massage(None, None, msg)
        print(f"return_code: {return_code}")
        self.assertEqual(return_code, 0)
        print(f"add_data: {comm.root.data.add_data}")
        print(comm.root.data.add_data.call_args)

    def test_wrong_keys(self):
        comm = comm_mqtt.MQTTComm(mock.Mock())
        msg = mqtt.MQTTMessage()
        msg.topic = b"Naresuan/Chatpon/data"
        msg.payload = b'{"datetTTTTtime": "2023-02-08 10:50:18", "device": "device 2", "temperature": 30}'
        return_code = comm.on_massage(None, None, msg)
        print(f"return_code: {return_code}")
        self.assertEqual(return_code, 310)


if __name__ == '__main__':
    unittest.main()