import random

def get_computer_move():
    moves = ["rock", "paper", "scissors"]
    return random.choice(moves)

def get_winner(player_move, computer_move):
    if player_move == computer_move:
        return "Tie"
    elif player_move == "rock" and computer_move == "scissors":
        return "Player"
    elif player_move == "paper" and computer_move == "rock":
        return "Player"
    elif player_move == "scissors" and computer_move == "paper":
        return "Player"
    else:
        return "Computer"

def play_game():
    player_move = input("Enter your move (rock, paper, or scissors): ")
    computer_move = get_computer_move()
    winner = get_winner(player_move, computer_move)
    print(f"You played {player_move} and the computer played {computer_move}.")
    print(f"The winner is {winner}.")

play_game()
