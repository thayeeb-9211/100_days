#Step 1 Pick a Random words and checking answer.
import random
word_list = ["apple", "mango", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
user = input("Guess a letter: ").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for guess in chosen_word:
  if guess == user:
    print("Right")
  else:
    print("wrong")