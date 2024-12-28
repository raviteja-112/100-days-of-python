from day12_art import logo
import random

def gamelogic(user, computer):
    if user > computer:
        print("Too high!")
        return True  # Guess is incorrect, return True
    elif computer > user:
        print("Too low!")
        return True  # Guess is incorrect, return True
    else:
        print(f"Congratulations! You guessed the correct number.The number is {computer}")
        return False  # Guess is correct, return False
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    noexit =tuple
    if level == 'easy':
        hearts = 10
    else:
        hearts = 5

    print(f"You have {hearts} attempts remaining to guess the number.")
    while hearts > 0 and noexit:
        guessednumber = int(input("Make a guess:"))
        noexit = gamelogic(guessednumber, number)  # Update noexit based on the result of gamelogic
        hearts = hearts - 1
        print(f"You have {hearts} attempts remaining to guess the number")


game()