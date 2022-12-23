# Copyright (C) 2022 Chatpon

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
from src.app import main_qui2


class TestStatusButton(unittest.TestCase):
    def test_toggle_color(self):
        status_button = main_qui2.StatusButton(None, "Chatpon")
        print(status_button)
        print(status_button.canvas.itemcget(status_button.circle,
                                            "fill"))
        print(status_button.color)
        print("===")
        status_button.toggle_color(True)
        print(status_button.canvas.itemcget(status_button.circle,
                                            "fill"))
        print(status_button.color)
        self.assertEqual(status_button.color, "green",
                         msg="Status color not change correctly ")


if __name__ == '__main__':
    unittest.main()
