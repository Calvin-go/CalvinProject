# simulate_dice_roll.py
import random

def roll_dice():
    return random.randint(1, 6)

if __name__ == "__main__":
    rolls = int(input("Enter the number of rolls: "))
    for _ in range(rolls):
        print(f"Rolled: {roll_dice()}")
