#Guess the number 
import random
print("Welcome to Guess that Number!")
guesses = 0
randomnum = random.randint(0, 10)

guess = int(input("Guess a number between 0 and 10: "))

while guess != randomnum:
    if guess == randomnum:
        print("You guessed the Number!!!!")
    elif guess > randomnum:
        print("Sorry, number to high")
    else guess < randomnum:
        print("Sorry, number to low!")
    break



