import random

print("Hello! What is your name?")
name = input()

print(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess")
number = random.randint(1, 20)

attemps = 0
while True:
    attemps += 1
    guess = int(input())
    
    if guess == number:
        print(f"Good job, {name}! You guessed my number in {attemps} guesses!")
        break
    elif guess < number:
        print(f"Your guess is too low.\nTake a guess")
        attemps += 1
    else :
        print(f"Your guess is too big.\nTake a guess.")
        attemps += 1