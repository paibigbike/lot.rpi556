# Copyright (C) 2023 Chatpon Chaimongkol <chatponc65@nu.ac.th>

"""

Make a graphical user interface with 1 button, that when pressed will publish to the HIVE MQTT broker
to the topic "Naresuan/Chatpon/Final", the message "Hello World"

"""

__author__ = "Chatpon Chaimongkol"

# library file
import tkinter as tk
import Comm_final


class Connect_to_Comm(tk.Tk):

    def __init__(self, master: Comm_final):
        self.comm = Comm_final.MQTTConn(self)
        self.app = master

        self.app.title("Communicated with Mqtt")  # Named to GUI

        # Create the buttons to Hello World

        self.button = tk.Button(self.app, text="Send Message", command=self.Send_message)
        self.button.pack()

        self.message = "Hello World"

    def Send_message(self):
        self.comm.publish(self.message)


if __name__ == "__main__":
    app = tk.Tk()
    app.geometry('400x400')  # size of gui
    Connect_to_Comm(app)
    app.mainloop()