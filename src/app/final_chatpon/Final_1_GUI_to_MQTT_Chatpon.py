# Copyright (C) 2023 Chatpon Chaimongkol <chatponc65@nu.ac.th>

"""

Make a graphical user interface with 1 button, that when pressed will publish to the HIVE MQTT broker
to the topic "Naresuan/Chatpon/Final", the message "Hello World"

"""

__author__ = "Chatpon Chaimongkol"

import tkinter as tk
import paho.mqtt.publish as publish


def send_message():

    topic = "Naresuan/Chatpon/Final"
    message = "2"
    publish.single(topic, message, hostname="broker.hivemq.com")
    print("Message sent to topic:", topic)


Tk = tk.Tk()
Tk.title("MQTT Publisher")

button = tk.Button(Tk, text="Send Message", command=send_message)
button.pack()

Tk.mainloop()

