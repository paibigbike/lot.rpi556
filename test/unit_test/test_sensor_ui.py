# Copyright (C) 2022 Chatpon Chaimongkol

"""



"""

__author__ = "Chatpon Chaimongkol"

# standard Libraries
import os
import sys
import unittest
from unittest import mock

sys.path.append(os.path.join("..", "..", "src", "app"))
# local file
from src.app import main_gui2


class TestSensorUI(unittest.TestCase):

    def test_button_click_change_running(self):
        gui = main_gui2.SensorUI()
        print(gui.running)
        self.assertFalse(gui.running)
        gui.button_click()
        print(gui.running)
        self.assertTrue(gui.running)

    def test_button_click_call_comm(self):

        with mock.patch("main_gui2.comm_mqtt.MQTTComm") as mocked_comm:
            gui = main_gui2.SensorUI()
            gui.button_click()
            gui.comm.publish.assert_called()
            gui.comm.publish: mock.MagicMock  # type printing
            gui.comm.publish.assert_called_with("on", is_data=False)


if __name__ == '__main__':
    unittest.main()

