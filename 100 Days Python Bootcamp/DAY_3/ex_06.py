# love calculator.

# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is *z*."
# e.g:
# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times

# Total = 5

# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times

# Total = 3

# Love Score = 53

# Print: "Your score is 53."

# Example Input 1
# Kanye West
# Kim Kardashian
# Example Output 1
# The Love Calculator is calculating your score...
# Your score is 42, you are alright together.


print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

combined = name1+ name2
lower = combined.lower()
t = lower.count("t")
r = lower.count("r")
u = lower.count("u")
e = lower.count("e")

first_digit = t+r+u+e

l = lower.count("l")
o = lower.count("o")
v = lower.count("v")
e = lower.count("e")

second_digit = l+o+v+e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")


# alternative_method/////////

def letter_counter(word, names):
    count = 0
    for letter in word:
        count += names.count(letter)

    return count

print("Welcome to the Love Calculator")
name1 = input("What is the name of the first person?\n>> ").lower()
name2 = input("What is the name of the second person?\n>> ").lower()

combined_names = name1 + name2

score = int(letter_counter('true', combined_names)) * 10\
        + letter_counter('love', combined_names)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos!")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")

