# Copyright (C) 2022 Chatpon

"""



"""

__author__ = "Chatpon Chaimongkol"


import tkinter as tk
import random


def rock():
    computer = random.choice(["rock", "paper", "scissors"])
    if computer == "rock":
        result.config(text="Tie!")
    elif computer == "paper":
        result.config(text="You lose!")
    elif computer == "scissors":
        result.config(text="You win!")


def paper():
    computer = random.choice(["rock", "paper", "scissors"])
    if computer == "rock":
        result.config(text="You win!")
    elif computer == "paper":
        result.config(text="Tie!")
    elif computer == "scissors":
        result.config(text="You lose!")


def scissors():
    computer = random.choice(["rock", "paper", "scissors"])
    if computer == "rock":
        result.config(text="You lose!")
    elif computer == "paper":
        result.config(text="You win!")
    elif computer == "scissors":
        result.config(text="Tie!")


root = tk.Tk()
root.title("Rock Paper Scissors")

rock_button = tk.Button(root, text="Rock", command=rock)
rock_button.pack()

paper_button = tk.Button(root, text="Paper", command=paper)
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", command=scissors)
scissors_button.pack()

result = tk.Label(root)
result.pack()
root.geometry('400x400')  # size
root.mainloop()
