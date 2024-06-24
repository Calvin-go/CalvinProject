# simple_number_guessing_game.py
import random

def guessing_game():
    number = random.randint(1, 100)
    guess = None

    while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
    print("Congratulations! You guessed it!")

if __name__ == "__main__":
    guessing_game()
