# Higher/Lower game

# ................<FLowchart Hints>.................

# to display art

# Generate a random data from the game data and compare them.

# print the random data directly with initalizing random data.

# Ask user for a guess.

# Check if user is correct.
# based upon follower count.
# If else Statement
# else give feedback

# Score must be continous.

# Game must repeat and also provide random data. ##so better is to define random data

# Clear screen between rounds and ask whether user wants to play or not. ## If/Else statement.
# repeat same process.

import random
import clear
from art import logo, vs
from game_data import data


def random_data():
  """Get data from random account"""
  return random.choice(data)
random_data1 = random_data()
random_data2 = random_data()

def check_answer(user, random_data1, random_data2):
  if random_data1["follower_count"] > random_data2["follower_count"]:
    return user == "a"
  else:
    return user == "b"
    
def game_is_on():
  print(logo)
  
  play_game = True
  score = 0
  
  while play_game:
    random_data1 = random_data()
    random_data2 = random_data()
    print("Compare A: ", random_data1["name"]+", " + random_data1["description"]+", with ", random_data1["follower_count"], "M followers, from",random_data1["country"])
    print(vs)
    print("Against B: ", random_data2["name"]+", " + random_data2["description"]+", with ", random_data2["follower_count"], "M followers, from",random_data2["country"])

    user = input("who has more followers? Type 'A' or 'B':").lower()
    checking = check_answer(user, random_data1, random_data2)
    clear()
    print(logo)
    if checking:
      score += 1
      print(f"'You are right!' Current score: {score}.")
    else:
      play_game = False
      print(f"'Sorry', that's wrong. Final score: {score}")
      print("You lose Game over...!!")
  return score

def play_game():
  while True:
    score = game_is_on()
    play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if play_again != 'yes':
        print("Goodbye!")
        break
    clear()

play_game()

# # Alternate Code.........
# import random
# from art import logo, vs
# from game_data import data


# def unique_choice(choice_a):

#     choice_b = random.choice(data)
#     while choice_b == choice_a:
#         choice_b = choice(data)

#     return choice_b

# def correct_answer(answer, followers_a, followers_b):

#     if answer == 'A':
#         return followers_a > followers_b
#     else:
#         return followers_b > followers_a


# score = 0
# first_question = True
# playing = True
# while playing:
#     print(logo)
#     if first_question:
#         choice_a = random.choice(data)
#     else:
#         choice_a = choice_b
#     print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")
#     print(vs)
#     choice_b = unique_choice(choice_a)
#     print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")
#     choice = input("Who has the more followers? Type 'A' or 'B': ").upper()
#     if correct_answer(choice, choice_a['follower_count'], choice_b['follower_count']):
#         score += 1
#         print(f"That is correct! Your score is {score}")
#         first_question = False
#     else:
#         print(f"Sorry, you were incorrect. Game over. Final score : {score}")
#         playing = False 