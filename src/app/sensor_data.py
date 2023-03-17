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


class SensorHubData:
    """
    Parent class to hold different sensor data series.

    sensor data series are held in the attribute dictionary sensor
    with the keys of "{device  data_type}" and values of SensorData , ie:
    {"device 2 temperature:SensorData "}

    Attributes:
        sensors (dict)

    """

    sensors = {}

    def __init__(self, _parent:tk.Tk):
        self.display = display.Display(_parent)
        self.display.pack()

    def add_data(self, sensor, time, temp):
        print(f"add data: {sensor}, {time} {temp}")
        sensor_key = f"{sensor} temp"
        print(sensor_key)
        if sensor_key not in self.sensors:
            print(f"add {sensor_key} to sensors")
            self.sensors[sensor_key] = Sensordata()
        _sensor_data = self.sensors[sensor_key]
        _sensor_data.add_data(time, temp)


        self.display.update_line(_sensor_data.time,
                                 _sensor_data.temperature,
                                 sensor)


@dataclass
class Sensordata:
    """

    Data class to hold 1 sensors time series data

    Attributes
        time(list[datetime]): time stamp of when ten sensor read data
        temperature (list[floats]): sensor data
        display(Display): child that will display the date of this class

    """
    def __init__(self):
        self.time = []
        self.temperature = []

    def add_data(self, time: datetime, temp: float):
        """

        Append new received data form a sensor and add it to the existing data.
        Call the Display child to update the user's view of the data

        """
        self.time.append(time)
        self.temperature.append(temp)
        # T000: fix this
        # self.display.update_line(self.time, self.temperature)
        # T000 fix


if __name__ == '__main__':
    parent = tk.Tk()
    sensor_data = Sensordata(parent)

    # use a lambda
    tk.Button(parent, text="update data",
              command=lambda: sensor_data.add_data(
                  datetime.now(), random.randrange(20, 35))
              ).pack()
    parent.mainloop()

