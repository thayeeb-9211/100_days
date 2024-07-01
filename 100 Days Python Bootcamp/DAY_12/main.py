# number guess


#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint
from art import logo

number = randint(1,101)
print("Welcome to the Number Guessing game..!!") 
print("I am thinking of a right number between 1 to 100. would you help me out in guessing the actual number?")
#Testing code
print(f'Pssst, the solution is {number}')

print(logo)
user = input("Choose the difficulty level you want..!! 'easy' or 'hard'?\n").lower()
easy_attempts = 10
hard_attempts = 5

def easy_game():
  attempts = easy_attempts
  while attempts > 0:
    guess = int(input("Make a guess: "))
    if guess == number:
      print(f"Congratulations! You guessed the number {number} correctly.")
      return
    elif guess < number:
      print("Too low.")
    else:
      print("Too high.")
    attempts -= 1
    print(f"You have {attempts} attempts remaining.")
  print("Game Over. You've run out of attempts.")

  
def hard_game():
  attempts = hard_attempts
  while attempts > 0:
    guess = int(input("Make a guess: "))
    if guess == number:
      print(f"Congratulations! You guessed the number {number} correctly.")
      return
    elif guess < number:
      print("Too low.")
    else:
      print("Too high.")
    attempts -= 1
    print(f"You have {attempts} attempts remaining.")
  print("Game Over. You've run out of attempts.")


while True:
  if user == 'easy':
    easy_game()
    break
  if user == 'hard':
    hard_game()
    break
  else:
      user = input("Invalid choice! Please choose 'easy' or 'hard': ").lower()
      
      
      
      
      
# #ALTERNATIVE_CODE.......!
# from random import randint
# EASY = 10
# HARD = 5

# secret_number = randint(1,100)
# print(secret_number)
# print("Welcome to the Number Guessing Game!")
# print("I am thinking of a number between 1 and 100.")
# difficulty_choice = input("Choose a difficulty. Type 'easy or 'hard': ")
# if difficulty_choice == 'easy':
#     attempts = EASY
# else:
#     attempts = HARD
# print(f"You have {attempts} attempts remaining to guess the number.")

# while attempts:
#     guess = int(input("Make a guess: "))
#     if guess == secret_number:
#         print(f"You win! You guessed my secret number with {attempts} attemptsleft.")
#         break
#     elif guess < secret_number:
#         print("Too low.\nGuess again")
#     else:
#         print("Too high.\nGuess again")
#     attempts -= 1
#     print(f"You have {attempts} attempts remaining to guess the number")
# if attempts == 0:
#     print(f"You lose! You have run out of attempts. My secret number was {secret_number}.")
