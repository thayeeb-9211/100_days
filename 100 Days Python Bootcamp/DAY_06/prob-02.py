### Project 2: Number Guessing Game
# **Description:** Create a number guessing game where the player has to guess a randomly generated number between 1 and 100.

#### Hints and TODOs:

# 1. **Generate Random Number**: Use the `random` module to generate a random number.

import random
number_to_guess = random.randint(1, 101)
  
# 2. **User Guess Loop**: Create a loop to take user guesses until the correct number is guessed.
attempts = 0
scenario = True
while scenario:
    guess = int(input("Guess the number (between 1 and 100): "))
    attempts += 1
        # TODO: Validate guess

# 3. **Give Hints**: Provide hints to the user whether their guess is too high or too low.
    # Validate guess and give hints
    if guess < 1 or guess > 100:
        scenario= False
        print("Invalid input. Please enter a number between 1 and 100.")
    elif guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
# 4. **Win Condition**: End the loop and congratulate the user when the correct number is guessed.
    elif guess == number_to_guess:
        print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        break

