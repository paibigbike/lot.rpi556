# Copyright (C) 2022 Chatpon Chaimongkol <chtponc65@nu.ac.th>

"""

Run unit test on the StatusButton class in the main_gui file

"""

__author__ = "Chatpon Chaimongkol"

# standard Libraries
import os
import sys
import unittest

print(os.getcwd())
print(os.path.abspath(os.path.join("..", "..", "src", "app")))
sys.path.append(os.path.join("..", "..", "src", "app"))
print(sys.path)


# local file
from src.app import main_gui2


class TestStatusButton(unittest.TestCase):
    def test_toggle_color(self):
        status_button = main_gui2.StatusButton(None, "Chatpon")
        color = status_button.canvas.itemcget(status_button.circle, "fill")
        self.assertEqual(color, "red",
                         msg="StatusButton not change correctly ")
        self.assertEqual(status_button.color, "red",
                         msg="Status color not change correctly ")

        status_button.toggle_color(True)
        color = status_button.canvas.itemcget(status_button.circle, "fill")

        self.assertEqual(color, "green",
                         msg="StatusButton not change correctly ")
        self.assertEqual(status_button.color, "green",
                         msg="Status color not change correctly ")

        status_button.toggle_color(False)
        color = status_button.canvas.itemcget(status_button.circle, "fill")

        self.assertEqual(color, "red",
                         msg="StatusButton not change correctly for false")
        self.assertEqual(status_button.color, "red",
                         msg="Status color not change correctly for false ")


if __name__ == '__main__':
    unittest.main()
