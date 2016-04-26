#!/usr/bin/env python
# This is a guess the number game.

import sys, random
#print(sys.version)


def die():
    print("I am thinking of a number between 1 and 20.")
    secretNumber = random.randint(1, 20)
    # Ask the player to guess 6 times.
    for i in range(1, 7):
        guess = int(input("Take a guess:    "))
        if guess > secretNumber:
            print("Your guess is too high. Take a guess.")
        elif guess < secretNumber:
            print("Your guess is too low. Take a guess.")
        else:
            break
    if guess == secretNumber:
        print("Good job! You guessed my secret number in %d guesses!" % (i))
    else:
        print('Nope. The secret number I was thinking of was ' + str(secretNumber))
    return(i)


if __name__ == '__main__':
    die()
