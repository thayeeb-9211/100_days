# Rock, Paper, Scissors
from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock; 1 for Paper;"
                          "2 for Scissors.\n>> "))
cpu_choice = randint(0,2)

print(f"Player chooses:\n {game_images[player_choice]}")
print(f"CPU chooses:\n {game_images[cpu_choice]}")

if player_choice == cpu_choice:
    print("It's a draw")
elif player_choice -1 == cpu_choice or player_choice + 2 == cpu_choice:
    print("You win!")
else:
    print("You lose!")

