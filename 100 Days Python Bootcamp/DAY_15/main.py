# Coffee Machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "pennies": 1,
    "nickels": 5,
    "dimes": 10,
    "quarters": 25,
}

money = 0


def print_report():

    print("Resources remaining:")
    for item, amount in resources.items():
        print(f"{item} : {amount}")
    print(f"Money : £{money:.2f}")
def sufficient_resources(drink_choice):

    for item, amount in MENU[drink_choice]['ingredients'].items():
        if resources[item] < amount:
            print(f"Sorry there is insufficient {item}.")
            return False
    return True

def take_money(total_money_inserted, cost):
    global money

    money += cost
    change = total_money_inserted - cost
    if change > cost:
        print(f"Here is your change, £{change:.2f}")
    else:
        print("Exact money given.")

def sufficient_money(drink_choice):

    total_money_inserted = 0
    for coin, value in coins.items():
        number_of_coins = int(input(f"How many {coin} added? "))
        total_money_inserted += value * number_of_coins

    total_money_inserted /= 100
    cost = MENU[drink_choice]['cost']
    if cost > total_money_inserted:
        return False
    else:
        take_money(total_money_inserted,cost)
        return True

def make_coffee(drink_choice):

    for item in MENU[drink_choice]['ingredients']:
        resources[item] -= MENU[drink_choice]['ingredients'][item]

power_on = True
while power_on:
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ")
    match drink_choice:
        case 'quit':
            print("Thank you. Powering down ..")
            power_on = False
        case 'report':
            print_report()
        case _:
            if sufficient_resources(drink_choice):
                if sufficient_money(drink_choice):
                    make_coffee(drink_choice)
                    print(f"Enjoy your {drink_choice}")
                else:
                    print("Insufficient funds. COINS RETURNED")
            else:
                print(f"Sorry {drink_choice} is unavailable")



