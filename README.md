# __Hangman - Portfolio Project 3__

![Hangman Game](/documentation/testing/mockup.png)

## How to play

* This is a Python terminal game and is deployed on Heroku using Code Institutes mock terminal template.
* Before starting the game the user is asked to enter their name and then gets a welcoming message before the game beginns.
* The user is then informed that they have 6 sttemps to guess a correct word before the game ends.
* If the user gets a correct letter their lives do not decrease but if the user types in a wrong letter their lives decreasee by one.
* The game will display a series of underscores, each representing a letter of the word to be guessed.
* Enter a letter to guess. If the letter is present in the word, the game will reveal its position(s) in the word.
* If the letter is not present in the word, the game will draw a body part of the hangman sketch.
* Continue guessing until either the word is correctly guessed or the stick figure is complete.
* if all letters are guesssed correctly the complete hangman sketch is not drawn and the user wins.
* the user looses by getting all 6 guesses wrong and thus the hangman sketch is drawn.
* when the game is over the user is prompted if they want to start a new game by choosing (y/n).
* If user chooses 'y' the game restarts and if user chooser 'n' the game ends with the message 'Thanks for playing hangman, see you next time'.

The deployed live game can be found at [Hangman Game](https://hang-men.herokuapp.com/)

### __User stories__

- As a player, I want to see a visual representation of the hangman so that I can keep track of my progress and know how many incorrect guesses I have left.
- As a player, I want to be able to see how many letters I need to guess.
- As a player, I want to be able to enter a letter guess so that I can try to guess the word.
- As a player, I want to see which letters I have already guessed so that I don't repeat the same letter.
- As a player, I want to receive feedback after each guess so that I know whether my guess was correct or not.
- As a player, I want to know how many letters are in the word so that I can make an informed guess.
- As a player, I want to be able to restart the game after the game has finished without exiting the program to do so.


