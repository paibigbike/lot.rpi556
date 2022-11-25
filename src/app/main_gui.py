# Copyright (C) 2022 Chatpon

"""Document string (Doc String)
A graphical user interface to observe sensor data
from a remote sensor through a mqtt communication channel
"""

__author__= "Chatpon Chaimongkol"

# Libraries / modules / packages
import tkinter

#make a variable to ch
color = 'green' # = assignment; assign 'red' to color

# make a python function to print "hello world"
# def - define
def hello_world():
    global color
    print("Hello World")
    if color == 'green': # == is a comparison
        color = 'yellow'
        #
    elif color== 'yellow':
        color = 'red'

    elif color == 'red':
        color = 'green'

    canvas.itemconfig(circle, fill=color)


app = tkinter.Tk() # appercation a class of tkinter.Tk
# geometry is a method of the tkinter.Tk class that
# sets the size of the app window . It takes a
# string as an argument.

app.geometry("400x400")
canvas = tkinter.Canvas(app, width=120, height=120)
circle = canvas.create_oval(10,10,110,110,
                            fill=color)
canvas.pack()

# make a button (tkinter class) and put it in the app
# Button take 2 arguments, app where to put the button
# text - key word argument

tkinter.Button(app, text= "hello world",
                          command=hello_world).pack()


app.mainloop() # mainloop is method of tkinter.Tk
#method