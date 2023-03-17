# Copyright (C) 2022 Chatpon

"""



"""

__author__ = "Chatpon Chaimongkol"

import tkinter as tk
import random


class RPSGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock Paper Scissors")

        # Create buttons for the user to select "rock," "paper," or "scissors"
        self.rock_button = tk.Button(self, text="Rock", command=lambda: self.play_game("rock"))
        self.rock_button.pack()
        self.paper_button = tk.Button(self, text="Paper", command=lambda: self.play_game("paper"))
        self.paper_button.pack()
        self.scissors_button = tk.Button(self, text="Scissors", command=lambda: self.play_game("scissors"))
        self.scissors_button.pack()

        # Create a label to display the results of the game
        self.result_label = tk.Label(self, text="Make your move")
        self.result_label.pack()

    def play_game(self, user_choice):
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)
        if user_choice == computer_choice:
            result = "Tie!"
        elif user_choice == "rock" and computer_choice == "scissors":
            result = "You win! Rock beats scissors."
        elif user_choice == "paper" and computer_choice == "rock":
            result = "You win! Paper beats rock."
        elif user_choice == "scissors" and computer_choice == "paper":
            result = "You win! Scissors beat paper."
        else:
            result = "You lose! {} beats {}.".format(computer_choice, user_choice)

        self.result_label.config(text=result)

if __name__ == "__main__":
    game = RPSGame()
    game.mainloop()
