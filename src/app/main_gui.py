# Copyright (C) 2022 Chatpon Chaimongkol

"""Document string (Doc String)
A graphical user interface to observe sensor data
from a remote sensor through a mqtt communication channel
"""

__author__ = "Chatpon Chaimongkol"

# Libraries / modules / packages
import tkinter


class StatusButton:
    """ Display the status using a canvas
            Attributes:
                circle : object used to display the status
                canvas (Tk.Canvas) : canvas the circle in
                color (str) : color the circle will show
    """
    def __init__(self, parent):

        self.color = 'red'
        self.canvas = tkinter.Canvas(parent, width=120, height=120)
        self.circle = self.canvas.create_oval(10, 10, 110, 110,
                                              fill=self.color)
        self.canvas.pack()

    def toggle_color(self):
        """ Toggle color between red and green """
        if self.color == 'red':  # == is a comparison
            self.color = 'yellow'
        elif self.color == 'yellow':
            self.color = 'green'
        elif self.color == 'green':
            self.color = 'red'

        self.canvas.itemconfig(self.circle, fill=self.color)


app = tkinter.Tk()  # appercation a class of tkinter.Tk
# geometry is a method of the tkinter.Tk class that
# sets the size of the app window . It takes a
# string as an argument.

app.geometry("400x400")
satus_btn = StatusButton(app)
print(satus_btn)
satus_btn2 = StatusButton(app)
print(satus_btn2)

# make a button (tkinter class) and put it in the app
# Button take 2 arguments, app where to put the button
# text - key word argument

tkinter.Button(app, text="Toggle Circle 1",
               command=satus_btn.toggle_color).pack()
tkinter.Button(app, text="Toggle Circle 1",
               command=satus_btn2.toggle_color).pack()

app.mainloop()  # mainloop is method of tkinter.Tk
# method
print('====')
print(satus_btn.toggle_color)
print(satus_btn.toggle_color())
