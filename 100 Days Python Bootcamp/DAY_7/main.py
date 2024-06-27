# Hangman
from hangman_art import stages, logo
from random import choice

words = ['apple', 'banana', 'coconut', 'damson']

already_guessed = []
correct_guesses = []
incorrect_guesses = []
def display():

    for letter in secret_word:
        if letter in correct_guesses:
            print(f"{letter} ", end='')
        else:
            print('_ ', end='')

    print(stages[lives])
    print(f"\nLives left: {lives}")
    print('Already chosen:')
    for letter in already_guessed:
        print(f"{letter} ", end=' ')

print(logo)
lives = 6
secret_word = choice(words)
playing = True
while playing:
    display()
    players_letter = input("\nChoose a letter\n>>")
    if players_letter in already_guessed:
        print(f"You have already chosen the letter {players_letter}")
        continue
    else:
        already_guessed.append(players_letter)

    if players_letter in secret_word:
        print("Well done you have found a letter from the secret word")
        correct_guesses.append(players_letter)
    else:
        print(f"The letter {players_letter} is not in the secret word.")
        incorrect_guesses.append(players_letter)
        lives -= 1

    if len(correct_guesses) == len(set(secret_word)):
        print(stages[lives])
        print(f"Congratulations! You have guessed my secret word, {secret_word}")
        playing = False
    if lives == 0:
        print(stages[lives])
        print(f"You lose! You ran out of lives. The secret word was {secret_word}")
        playing = False


