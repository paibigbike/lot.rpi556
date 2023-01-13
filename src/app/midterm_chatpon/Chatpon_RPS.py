# Copyright (C) 2022 Chatpon Chaimongkol <chatponc65@nu.ac.th>

"""

Make a GUI to play Rock Paper Scissor over the internet

"""

__author__ = "Chatpon Chaimongkol"

# standard libra
import tkinter as tk
import Chatpon_comm  # MQTT
import random


class Rock_Paper_Scissors(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.comm = Chatpon_comm.MQTTConn(self)  # MQTT

        # Rock
        self.rock_button = tk.Button(self, text="Rock",
                                     font=20, command=self.rock)
        self.rock_button.pack()

        # Scissors
        self.scissors_button = tk.Button(self, text="Scissors",
                                         font=20, command=self.scissors)
        self.scissors_button.pack()

        # Paper
        self.paper_button = tk.Button(self, text="Paper",
                                      font=20, command=self.paper)
        self.paper_button.pack()

        self.player_choice = " "

        self.result_user = tk.Label(self, text="")
        self.result_user.pack()

        self.result_AI = tk.Label(self, text="")
        self.result_AI.pack()

        self.result = tk.Label(self, text="")
        self.result.pack()

    def rock(self):
        """
        Toggle the stat of the sensor True -> False or False -> True,
        update the text of the run button, update the local StatusButton,
        and send the proper mqtt message

        """
        self.player_choice = 'Rock'
        self.result_user.config(text="You picked Rock", font=20)

        msg1 = "Player pick Rock"  # MQTT
        self.comm.publish(msg1)    # MQTT
        computer = random.choice(["rock", "paper", "scissors"])

        if computer == "rock":
            self.result_AI.config(text="Com picked Rock", font=20)
            msg2 = "Com pick Rock"  # MQTT
            self.comm.publish(msg2)  # MQTT

            self.result.config(text="Tie!", font=42)
            msg3 = "Tie"  # MQTT
            self.comm.publish(msg3)  # MQTT

        elif computer == "paper":
            self.result_AI.config(text="Com picked Paper", font=20)
            msg2 = "Com pick Paper"  # MQTT
            self.comm.publish(msg2)  # MQTT

            self.result.config(text="You lose!", font=42)
            msg3 = "You lose!"  # MQTT
            self.comm.publish(msg3)  # MQTT

        elif computer == "scissors":
            self.result_AI.config(text="Com picked Scissors", font=20)
            msg2 = "Com pick Scissors"  # MQTT
            self.comm.publish(msg2)  # MQTT

            self.result.config(text="You win!", font=42)
            msg3 = "You win!"  # MQTT
            self.comm.publish(msg3)  # MQTT

    def scissors(self):
        self.player_choice = 'Scissors'
        self.result_user.config(text="You picked Scissors", font=20)

        msg1 = "Scissors"  # MQTT
        self.comm.publish(msg1)  # MQTT
        computer = random.choice(["rock", "paper", "scissors"])

        if computer == "rock":
            self.result_AI.config(text="Com picked Rock", font=20)
            msg2 = "Com pick Rock"  # MQTT
            self.comm.publish(msg2)  # MQTT

            self.result.config(text="You lose!", font=42)
            msg3 = "You lose!"  # MQTT
            self.comm.publish(msg3)  # MQTT

        elif computer == "paper":
            self.result_AI.config(text="Com picked Paper", font=20)
            msg2 = "Com pick Paper"  # MQTT
            self.comm.publish(msg2)  # MQTT

            self.result.config(text="You win!", font=42)
            msg3 = "You win!"  # MQTT
            self.comm.publish(msg3)  # MQTT

        elif computer == "scissors":
            self.result_AI.config(text="Com picked Scissors", font=20)
            msg2 = "Com pick Scissors"  # MQTT
            self.comm.publish(msg2)  # MQTT

            self.result.config(text="Tie!", font=42)
            msg3 = "Tie"  # MQTT
            self.comm.publish(msg3)  # MQTT

    def paper(self):
        self.player_choice = 'Paper'
        self.result_user.config(text="You picked Paper", font=20)

        msg1 = "Paper"  # MQTT
        self.comm.publish(msg1)  # MQTT
        computer = random.choice(["rock", "paper", "scissors"])

        if computer == "rock":
            self.result_AI.config(text="Com picked Rock", font=20)
            msg2 = "Com pick Rock"  # MQTT
            self.comm.publish(msg2)  # MQTT

            self.result.config(text="You win!", font=42)
            msg3 = "You win!"  # MQTT
            self.comm.publish(msg3)  # MQTT

        elif computer == "paper":
            self.result_AI.config(text="Com picked Paper", font=20)
            msg2 = "Com pick Paper"  # MQTT
            self.comm.publish(msg2)  # MQTT

            self.result.config(text="Tie!", font=42)
            msg3 = "Tie"  # MQTT
            self.comm.publish(msg3)  # MQTT

        elif computer == "scissors":
            self.result_AI.config(text="Com picked Scissors", font=20)
            msg2 = "Com pick Scissors"  # MQTT
            self.comm.publish(msg2)  # MQTT

            self.result.config(text="You lose!", font=42)
            msg3 = "You lose!"  # MQTT
            self.comm.publish(msg3)  # MQTT


if __name__ == "__main__":
    app = Rock_Paper_Scissors()   # application a class ot tkinter.Tk
    # geometry is a method of the tkinter.Tk class that
    # sets the size of the app window. It takes a
    # string as on argument
    app.geometry("400x400")
    app.title('Rock Paper Scissors game')
    app.mainloop()  # mainloop is method of tkinter.Tk
    # methods are function of cla