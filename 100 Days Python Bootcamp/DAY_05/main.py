# Password Generator
from random import choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def choose_characters(character_set, required):

    characters = []
    for _ in range(required):
        characters.append(choice(character_set))

    return characters

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n>>"))
num_numbers = int(input("How many numbers would you like in your password?\n>>"))
num_symbols = int(input("How many symbols would you like in your password?\n>>"))

password = choose_characters(letters, num_letters) \
           + choose_characters(numbers, num_numbers)\
           + choose_characters(symbols, num_symbols)
shuffle(password)
password = ''.join(password)

print(f"Your password is: {password}")