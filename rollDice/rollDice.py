import random

def rollDice():
    num_rolled = random.randint(1,6)
    return num_rolled

def main():
    decision = "Y"
    while decision == "Y" or decision == "y":
        print(rollDice())
        decision = input("Roll the dice again? (Y/N): ")
main()





