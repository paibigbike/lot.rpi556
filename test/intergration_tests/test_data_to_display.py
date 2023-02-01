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

sys.path.append(os.path.join("..", "..", "src", "app"))
# local file
from src.app import display
from src.app import sensor_data


class TestDataToDisplay(unittest.TestCase):
   def test_data_to_diplay(self):
       """

       Test that adding data to the data class make the
       pylot graph have correct xy data

       """
       sensor_class = sensor_data.Sensordata(None)
       print(sensor_class)
       # add 1 data point and check is is added correctly
       now = datetime(2023, 1, 24, 10, 50, 12)
       sensor_class.add_data(now, 5)
       print(f"sensor.display: {type(sensor_class.display)}")
       start_time = datetime(1978, 1, 1)
       print(f"start_time: {start_time}")
       print(f"diff: {start_time.now}")
       xy_data = sensor_class.display.lines[0].get_xydata().tolist()
       print(f"plt data; {xy_data}")
       print(f"xy data type: {type(xy_data)}")
       # T000: claculate how datetime is converted is a float
       self.assertEqual([[19381.45152777778, 5.0]], xy_data)





if __name__ == '__main__':
    unittest.main()