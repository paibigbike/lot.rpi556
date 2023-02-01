# Copyright (C) 2023 Chatpon Chaimongkol <chatponc65@nu.ac.th>

"""

Fill in the unit test for the display.Display method of update_line

"""

__author__ = "Chatpon Chaimongkol"

# standard libraries
from datetime import datetime
import os
import sys
import unittest

sys.path.append(os.path.join("..", "..", "src", "app"))
# local files
from src.app import display


class TestDisplay(unittest.TestCase):
    def test_update_line(self):
        """ Test that calling the update_line method
        in display.Display works correctly """
        _display = display.Display(None)
        time = [datetime(2023, 1, 24, 10, 50, 12)]
        temps = [5]
        _display.update_line(time, temps)
        print("getting x y data")
        print(_display.lines[0].get_xydata())
        # assignment: use asserts to check update_line works correctly
        xy_data = _display.lines[0].get_xydata().tolist()
        print(f"plt data; {xy_data}")
        print(f"xy data type: {type(xy_data)}")
        self.assertEqual([[19381.45152777778, 5.0]], xy_data)




if __name__ == '__main__':
    unittest.main()