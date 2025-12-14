Bulls & Cows (Python)

A simple console implementation of the classic Bulls & Cows guessing game written in Python.

The program generates a secret 4-digit number and the player tries to guess it.
After each guess, the game reports how many bulls and cows the guess contains.

Game Rules

The secret number:

  -has exactly 4 digits

  -contains unique digits (no duplicates)

  -does not start with zero (0)

A bull means:

 -correct digit in the correct position

A cow means:

 -correct digit but in the wrong position

bull positions are never counted as cows

How to Play

Run the program:

python main.py


Enter a 4-digit guess.

The game will validate your input and respond with:

number of bulls

number of cows

Keep guessing until you find the secret number.

After each game, you can choose to play again.

Example Output
>>> 1234
0 bulls, 2 cows
-----------------------------------------------
>>> 2017
Correct, you've guessed the right number
in 4 guesses!
-----------------------------------------------
That's amazing!

Features

Input validation with clear error messages

Correct bull/cow counting

Pluralized output (1 bull vs 2 bulls)

Game statistics (number of guesses per game)

Optional hidden developer command:

"__dev__" without "


Displays the secret number (does not count as a guess)

Requirements

Python 3.10+

Standard library only (no external dependencies)
