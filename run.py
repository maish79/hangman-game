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
    

def update_blank(guess, word, blank):
    """
    Updates the blank spaces with the newly guessed
    letter if it is present in the word.
    Returns the updated blank spaces.
    """
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                blank[i] = guess
        print("Congrats you found a match")
    else:
        print(f"Sorry, {guess} is not in the word. Please, try again!")
    return blank

