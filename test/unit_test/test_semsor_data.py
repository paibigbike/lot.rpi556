# Copyright (C) 2023 Chatpon Chaimongkol <chatponc65@nu.ac.th>

"""

Test the methods of the sensor_data.Sensordata class

"""

__author__ = "Chatpon Chaimongkol"

# standard Libraries
from datetime import datetime
import os
import sys
import unittest
from unittest import mock

sys.path.append(os.path.join("../../src", "..", "src", "app"))
# local file
from src.app import sensor_data


class TestSensorData(unittest.TestCase):
    def setUp(self) -> None:
        """ for each test, make the sensor class, initialize the temperature
        and time variables and mock the display and put in self to use for tests"""
        with mock.patch("sensor_data.Sensordata") as mock_display:
            self.sensor_class = sensor_data.SensorHubData(None)
            print(self.sensor_class.sensors)
            print('=====')
            for _key in self.sensor_class.sensors:
                _sensor_data = self.sensor_class.sensors[_key]
                print(_sensor_data)
                _sensor_data.temperature = []
                _sensor_data.time = []
            self.mock_display = mock_display

    def test_add_data(self):
        sensor_class = self.sensor_class
        print(sensor_class)

        now = datetime(2023, 1, 24, 10, 50, 12)
        print(f"start: {sensor_class.sensors}")
        print(now)
        sensor_class.add_data("device2", now, 5)
        print(f"middle: {sensor_class.sensors}")
        print(f'time: (sensor_class.time)')
        print(f'temp: (sensor_class.temperature)')
        self.assertTrue('device2 temp' in sensor_class.sensors)
        sensor = sensor_class.sensors["device2 temp"]
        self.assertEqual([now], sensor.time)
        self.assertEqual([5], sensor.temperature)

        # Add second data print
        now2 = datetime(2023, 1, 24, 10, 50, 12)
        sensor_class.add_data("device 2", now2, 10)
        print(f'time: (sensor_class.time)')
        print(f'temp: (sensor_class.temperature)')
        self.assertEqual([now, now2], sensor.time)
        self.assertEqual([5, 10], sensor.temperature)

     # T000: Move this test to TestSensorHubData

    #def test_display_update_line_calleded(self):
        """

        Test that update_line method is call correctly.
        Use the test_sensor

        """

       # sensor_class = self.sensor_class

        # mock the display.Display class in the sensor_data module
        #now = datetime(2023, 1, 24, 10, 50, 12)
       # sensor_class.add_data("device 2",now, 5)
        #
       # sensor_class.display.update_line.assert_called_with([now], [5])
        #with mock.patch("sensor_data.Sensordata") as sensor_class:
          ### sensor_class = sensor_data.Sensordata(None)
          ###print('======')
          ###print(sensor_class.add_data)
           ## sensor_class = sensor_data.Sensordata(None)
            #print(sensor_class)
            #
            #now = datetime(2023, 1, 24, 10, 50, 12)
            #sensor_class.add_data(now, 5)
             # check that the self.display.update_line is called with the
    
            #print(f"update_line: {sensor_class.display.update_line}")
            #print(f"arg: {self.mock_display.update_line.call_args}")
            #print(f"arg2: {sensor_class.display.update_line.call_args}")
            #print(self.mock_display)
            #sensor_class.display.update_line.assert_called_with([now], [5])


class TestSensorHubData(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()