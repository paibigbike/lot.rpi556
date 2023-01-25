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
import sensor_data

sys.path.append(os.path.join("..", "..", "src", "app"))
# local file
from src.app import main_gui2


class TestSensorData(unittest.TestCase):
    def test_add_data(self):
        sensor_class = sensor_data.Sensordata(None)
        print(sensor_class)

        now = datetime(2023, 1, 24, 10, 50, 12)
        print(now)
        sensor_class.add_data(now, 5)
        print(f'time: (sensor_class.time)')
        print(f'temp: (sensor_class.temperature)')
        self.assertEqual([now], sensor_class.time)
        self.assertEqual([5], sensor_class.temperature)

        now2 = datetime(2023, 1, 24, 10, 50, 12)
        sensor_class.add_data(now2, 10)
        print(f'time: (sensor_class.time)')
        print(f'temp: (sensor_class.temperature)')
        self.assertEqual([now, now2], sensor_class.time)
        self.assertEqual([5, 10], sensor_class.temperature)


if __name__ == '__main__':
    unittest.main()