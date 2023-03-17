# Copyright (C) 2023 Chatpon Chaimongkol <chatponc65@nu.ac.th>

"""

Test that when data is input to the sensor_data.Sensor
it is passed and handled correctly by the display.Display

"""

__author__ = "Chatpon Chaimongkol"

# standard Libraries
from datetime import datetime
import os
import sys
import unittest
from unittest import mock

sys.path.append(os.path.join("..", "..", "src", "app"))
# local file
from src.app import sensor_data


class TestDataToDisplay(unittest.TestCase):
   def test_data_to_display(self):
       """

       Test that adding data to the data class make the
       pylot graph have correct xy data

       """
       sensor_class = sensor_data.SensorHubData(None)
       print(sensor_class)

       #add 1 data point and check is is added correctly
       now = datetime(2023, 1, 24, 10, 50, 12)
       sensor_class.add_data("device 2 temp", now, 5)
       xy_data = sensor_class.display.lines["device 2 temp"].get_xydata().tolist()

       # T000: calculate how datetime is converted is a float
       self.assertEqual([[19381.45152777778, 5.0]], xy_data)

   def test_draw_is_called(self):
       # initialize the sensor_class
       sensor_class = sensor_data.SensorHubData(None)
       # to check if a method is called mock it first
       sensor_class.display.canvas.draw = mock.Mock()
       now = datetime(2023, 1, 24, 10, 50, 12)
       sensor_class.add_data("device 2", now, 5)
       # check that the draw function is called
       sensor_class.display.canvas.draw.assert_called()


if __name__ == '__main__':
    unittest.main()