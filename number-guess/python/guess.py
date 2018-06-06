# This is a guess the number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20) # TODO what if we want a different range?
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6: # TODO What if we want more or less guesses?
    print('Take a guess.') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    # TODO Lets make it so that the program tells us if the gues is too high or too low.

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)