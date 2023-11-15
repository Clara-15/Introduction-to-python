#Write a program that asks a user to guess the value of a number chosen between 1 and 99. 
#Let the user know if their guess is too low, too high, or correct.

import random

# Generate a random number between 1 and 99
secret_number = random.randint(1, 99)

# Flag to check if the user has guessed correctly
correct_guess = False

# Keep prompting the user until they guess correctly
while not correct_guess:
    # Ask the user for input
    user_guess = int(input("Guess the number between 1 and 99: "))

    # Check the user's guess
    if user_guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        correct_guess = True
    elif user_guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
