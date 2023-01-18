# Copyright (C) 2023 Chatpon Chaimongkol <chtponc65@nu.ac.th>

"""

Display the data cosing to from the sensor
Wrap a matplotlib pyplot in a tkinter frame

"""

__author__ = "Chatpon Chaimongkol"


# standard library
from dataclasses import dataclass
from datetime import datetime
import random
import tkinter as tk

# installed library
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
x =[1, 2, 3, 4, 5]
y =[10, 20, 40, 80, 160]


class Display(tk.Frame):
    def __init__(self, parent: tk.Tk):
        tk.Frame.__init__(self, master=parent)
        self.figure = plt.figure(figsize=(6, 4))
        self.axis = self.figure.add_subplot()
        plot_return = self.axis.plot(x, y)
        canvas = FigureCanvasTkAgg(self.figure, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack()
        self.pack()


@dataclass
class Sensordata:
    time = []
    Temperature = []

    def __init__(self, _parent):
        self.display = Display(_parent)
        self.display.pack()

    def add_data(self):
        self.time.append(datetime.now())
        self.Temperature.append(random.randrange(20, 35))
        print(self.time)
        print(self.Temperature)


if __name__ == '__main__':
    parent = tk.Tk()
    sensor_data = Sensordata(parent)
    tk.Button(parent, text="update data",
              command=sensor_data.add_data).pack()
    parent.mainloop()

