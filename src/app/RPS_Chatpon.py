# Copyright (C) 2022 Chatpon Chaimongkol <chatponc65@nu.ac.th>

"""

Make a GUI to play Rock Paper Scissor over the internet

"""

__author__ = "Chatpon Chaimongkol"

# Libraries / modules / packages
import tkinter as tk


class Rock_Paper_Scissors:
    """ make class to create GUI """

    def __init__(self, rps_game):
        self.app = rps_game
        self.app.title("Rock Paper Scissors game")  # Named to GUI

        # Rock
        self.rock_button = tk.Button(self.app, text="Rock", font=42, command=self.rock)
        self.rock_button.pack()

        # Scissors
        self.scissors_button = tk.Button(self.app, text="Scissors",  font=42, command=self.scissors)
        self.scissors_button.pack()

        # Paper
        self.paper_button = tk.Button(self.app, text="Paper", font=42, command=self.paper)
        self.paper_button.pack()

        # Create text for showing results

        self.result = tk.Label(self.app, text="")
        self.result.pack()

    def rock(self):
        """ It will show text as 'You picked Rock' """
        self.result.config(text="You picked Rock", font=42)

    def scissors(self):
        """  It will show text as 'You picked Scissors' """
        self.result.config(text="You picked Scissors", font=42)

    def paper(self):
        """ It will show text as 'You picked Paper' """
        self.result.config(text="You picked Paper", font=42)


app = tk.Tk()
app.geometry('400x400')  # size
Rock_Paper_Scissors(app)
app.mainloop()
