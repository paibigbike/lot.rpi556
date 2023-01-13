# Copyright (C) 2022 Chatpon Chaimongkol <chatponc65@nu.ac.th>

"""

Make a GUI to play Rock Paper Scissor over the internet

"""

__author__ = "Chatpon Chaimongkol"

# Libraries / modules / packages
import tkinter as tk

import random

# local files
import comm_mqtt_for_RPS


class RockPaperScissors(tk.Tk):
    """ make class to create GUI """

    def __init__(self, rps_game):

        self.comm = comm_mqtt_for_RPS(self)

        self.app = rps_game
        self.app.title("Rock Paper Scissors game")  # Named to GUI

        # Rock
        self.rock_button = tk.Button(self.app, text="Rock", font=20, command=self.rock)
        self.rock_button.pack()

        # Scissors
        self.scissors_button = tk.Button(self.app, text="Scissors",  font=20, command=self.scissors)
        self.scissors_button.pack()

        # Paper
        self.paper_button = tk.Button(self.app, text="Paper", font=20, command=self.paper)
        self.paper_button.pack()

        self.player_choice = " "

        # Create text for showing results

        self.result_user = tk.Label(self.app, text="")
        self.result_user.pack()

        self.result_AI = tk.Label(self.app, text="")
        self.result_AI.pack()

        self.result = tk.Label(self.app, text="")
        self.result.pack()

    def rock(self):
        """ It will show text as 'You picked Rock' """
        self.player_choice = 'Rock'
        self.result_user.config(text="You picked Rock", font=20)
        #computer = random.choice(["rock", "paper", "scissors"])

        #if computer == "rock":
           # self.result_AI.config(text="Com picked Rock", font=20)
            result.config(text="Tie!", font=42)
        #elif computer == "paper":
            self.result_AI.config(text="Com picked Paper", font=20)
            result.config(text="You lose!", font=42)
        #elif computer == "scissors":
            self.result_AI.config(text="Com picked Scissors", font=20)
            result.config(text="You win!", font=42)


        #msg = "result"
        #self.comm.publish(msg)  # MQTT

        #self.msg = self.player_choice
        #self.comm.publish(self.msg)

    def scissors(self):
        """  It will show text as 'You picked Scissors' """
        self.player_choice = 'Scissors'
        self.result_user.config(text="You picked Scissors", font=20)
        #computer = random.choice(["rock", "paper", "scissors"])

        #if computer == "rock":
            self.result_AI.config(text="Com picked Rock", font=20)
            result.config(text="You lose!", font=42)

        #elif computer == "paper":
            self.result_AI.config(text="Com picked Paper", font=20)
            result.config(text="You win!", font=42)

        #elif computer == "scissors":
            self.result_AI.config(text="Com picked Scissors", font=20)
            result.config(text="Tie!", font=42)

        #msg = "result"
        #self.comm.publish(msg)  # MQTT
        #self.msg = self.player_choice
        #self.comm.publish(self.msg)

    def paper(self):
        """ It will show text as 'You picked Paper' """
        self.player_choice = 'Paper'
        self.result_user.config(text="You picked Paper", font=20)
        #computer = random.choice(["rock", "paper", "scissors"])

        #if computer == "rock":
            #self.result_AI.config(text="Com picked Rock", font=20)
            #result.config(text="You win!", font=42)

        #elif computer == "paper":
            #self.result_AI.config(text="Com picked Paper", font=20)
           # result.config(text="Tie!", font=42)

       # elif computer == "scissors":
           # self.result_AI.config(text="Com picked Scissors", font=20)
            #result.config(text="You lose!", font=42)

        #msg = "result"
        #self.comm.publish(msg)  # MQTT
        #self.msg = self.player_choice
        #self.comm.publish(self.msg)


# app = Rock_Paper_Scissors  # appercation a class of tkinter.Tk
if __name__ == "__main__":
    app = tk.Tk()
    app.geometry('400x400')  # size of gui
    RockPaperScissors(app)
    result = tk.Label(app)
    result.pack()
    app.mainloop()



