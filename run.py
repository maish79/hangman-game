"""
importing modules for hangman game

"""

import random
import pyfiglet
import hangman_letters


def display_logo():
    """ Displays the hangman logo """
    logo = pyfiglet.figlet_format("welcome to\n Hangman",
                                  font="standard", justify="center")
    print(logo)


def get_player_name():
    """Prompts the player to enter their name and returns the name"""
    player_name = input("Please enter your name: ")
    return player_name


name = get_player_name()
print("Hello, " + name + "! Welcome to the game")


def update_guessed(guess, guessed):
    """Updates the guessed letters with the newly guessed letter"""
    return guessed + guess
