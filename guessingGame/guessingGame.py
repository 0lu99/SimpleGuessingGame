import random

secretNumber = random.randint(1, 5)
guessCounter = 0
guessLimit = 3

while guessCounter < 3:
    userGuess = int(input("Guess the number: "))
    guessCounter += 1
    if userGuess == secretNumber:
        print("You won!")
        break
else:
    print(f"You had 3 guesses and failed. The number was {secretNumber}")