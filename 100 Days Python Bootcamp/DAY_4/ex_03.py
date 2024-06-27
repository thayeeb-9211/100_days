# Banker Roulette

# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.
# NOTE: In this exercise, you are working collaboratively with another programmer. 
# They already dealt with input() and writing the code needed to get hold of the names in the input area, so you don't need to worry about that.
# The other programmer has written the code to separate the names in the input area into individual names and puts them inside a List called names. 
# For their code to work correctly, you must enter all the names in the input area followed by comma then space. e.g. name, name, name


# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.

# Example Output
# Michael is going to buy the meal today!

# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs

# import random
# names = names_string.split(", ")
# num_items =len(names)
# random_name = random.randint(0, num_items-1)
# print(names[random_name]+" is going to buy the meal today!") 

# alternative_method...

from random import choice, randint

diners = input("Can I have the diners names?\n>> ")
diners_lst = diners.split(', ')

paying_diner = choice(diners_lst)
print(f"{paying_diner} will get the bill")

paying_diner = diners_lst[randint(0,len(diners_lst)-1)]
print(f"{paying_diner} will get the bill")
