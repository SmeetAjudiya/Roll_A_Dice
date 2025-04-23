import random

def roll_a_dice():
    return random.randint(1,6)

def main():
    while True:
        print("Rolling Dice")

        result = roll_a_dice()
        print(f"The value is: {result}")

        repeat = input("Roll the dice again (y/n):").strip().lower()

        if repeat != 'y':
            print("Thank you for playing !!")
            break

if __name__ == "__main__":
    main()