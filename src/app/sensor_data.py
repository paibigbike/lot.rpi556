# Copyright (C) 2023 Chatpon Chaimongkol <chatponc65@nu.ac.th>

"""



"""

__author__ = "Chatpon Chaimongkol"

from dataclasses import dataclass
from datetime import datetime
import random
import tkinter as tk

# local file
import display


@dataclass
class Sensordata:
    """

    Data class to hold 1 sensors time series data

    Attributes
        time(list[datetime]): time stamp of when ten sensor read data
        temperature (list[floats]): sensor data
        display(Display): child that will display the date of this class

    """
    time = []
    temperature = []

    def __init__(self, _parent):
        self.display = display.Display(_parent)
        self.display.pack()

    def add_data(self, time: datetime, temp: float):
        """

        Append new received data form a sensor and add it to the existing data.
        Call the Display child to update the user's view of the data

        """
        self.time.append(time)
        self.temperature.append(temp)
        self.display.update_line(self.time, self.temperature)


if __name__ == '__main__':
    parent = tk.Tk()
    sensor_data = Sensordata(parent)

    # use a lambda
    tk.Button(parent, text="update data",
              command=lambda: sensor_data.add_data(
                  datetime.now(), random.randrange(20 ,35))
              ).pack()
    parent.mainloop()

