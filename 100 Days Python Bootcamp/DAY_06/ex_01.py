from random import randint

def eating():

    print("Nom-Nom")

hungry = True
still_hungry = 6
while hungry:
    eating()
    if still_hungry == randint(1,6):
        hungry = False