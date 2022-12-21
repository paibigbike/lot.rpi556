# Copyright (C) 2022 Chatpon Chaimongkol

"""Document string (Doc String)
A graphical user interface to observe sensor data
from a remote sensor through a mqtt communication channel
"""

__author__ = "Chatpon Chaimongkol"

# Libraries / modules / packages
import tkinter as tk

# local files
import comm_mqtt

NAME = ["Kyle", "Chatpon", "Tao", "Sudarat"]


class SensorUI(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)  # initialize parent class
        self.comm = comm_mqtt.MQTTConn(self)
        status_frame = tk.Frame(self, relief=tk.RIDGE, borderwidth=5)
        self.status_buttons = []
        print("1: ", self.status_buttons)
        for i in range(4):
            status_btn = StatusButton(status_frame, NAME[i])
            self.status_buttons.append(status_btn)
        status_frame.pack(side=tk.TOP)
        # make a button (tkinter class) and put it in the app
        # Button take 2 arguments, app where to put the button
        # text - key word argument
        self.running = False
        self.button = tk.Button(self, text="Turn on",
                  command = self.button_click)
        self.button.pack(side=tk.TOP)

    def button_click(self):
        if self.running: # if True turn off the sensor
            self.running = False
            msg = "off"
            self.button.config(text="turn om")

        else:
            self.running = True
            msg = "on"
            self.button.config(text="turn off")
        self.change_status("Chatpon", self.running)
        #index = NAME.index("Chatpon")
        self.comm.publish(msg)

    def change_status(self, name, _running):
        index = NAME.index(name)
        self.status_buttons[index].toggle_color(_running)

class StatusButton(tk.Frame):
    """ Display the status using a canvas
            Attributes:
                circle : object used to display the status
                canvas (Tk.Canvas) : canvas the circle in
                color (str) : color the circle will show
    """

    def __init__(self, parent, name):
        tk.Frame.__init__(self, master=parent)
        self.color = 'red'
        self.canvas = tk.Canvas(self, width=120, height=120)
        self.circle = self.canvas.create_oval(10, 10, 110, 110,
                                              fill=self.color)
        self.canvas.pack(side=tk.TOP)
        tk.Label(self, text=name, font=42).pack(side=tk.TOP)
        self.pack(side=tk.LEFT)

    def toggle_color(self, state):
        """ Toggle color between red and green """
        if state:
            self.color = 'green'
        else:
            self.color = 'red'

        self.canvas.itemconfig(self.circle, fill=self.color)


if __name__ == '__main__':
    app = SensorUI()  # appercation a class of tkinter.Tk
    # app2 = SensorUI()
    # geometry is a method of the tkinter.Tk class that
    # sets the size of the app window . It takes a
    # string as an argument.

    app.geometry("600x400")
    # app2.geometry("400x400")
    app.mainloop()  # mainloop is method of tkinter.Tk
    # method
