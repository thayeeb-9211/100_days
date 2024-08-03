# Coffee Machine

MENU = {
    "espresso [a]": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5, #dollars
    },
    "latte [b]": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5, #dollars
    },
    "cappuccino [c]": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0, #dollars
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print("""
 ██████  ██████  ███████ ███████ ███████ ███████     ███    ███  █████   ██████ ██   ██ ██ ███    ██ ███████ 
██      ██    ██ ██      ██      ██      ██          ████  ████ ██   ██ ██      ██   ██ ██ ████   ██ ██      
██      ██    ██ █████   █████   █████   █████       ██ ████ ██ ███████ ██      ███████ ██ ██ ██  ██ █████   
██      ██    ██ ██      ██      ██      ██          ██  ██  ██ ██   ██ ██      ██   ██ ██ ██  ██ ██ ██      
 ██████  ██████  ██      ██      ███████ ███████     ██      ██ ██   ██  ██████ ██   ██ ██ ██   ████ ███████ \n              
                                          😁😋☕ ♨️  😍😘🥰
                                                                                                             
                                                                                                             
""")

def process_coins():
    print("Please insert coins.")
    #converted input to integer and multiplied with the given value of the coins.
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.1
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    sum = quarters + dimes + nickles + pennies
    return sum
make_coffee = True
while make_coffee:
    #defined a choice_map so that the user can easily enter the prompt in alphabets and also for me to call them in loops.
    def choice_map(choice):
        choice_map = {
                "a": "espresso [a]",
                "b": "latte [b]",
                "c": "cappuccino [c]"
            } 
        money = 0
        #defined a resource funtion so that it can be called after the successfull transaction and give reports all time.
        def resource():
                print(f"\nWater: {resources['water']}ml")
                print(f"Milk: {resources['milk']}ml")
                print(f"Coffee: {resources['coffee']}g")
                print(f"Money: ${money}")
            
        if user == 'off':
         make_coffee = False
            
        elif user in choice_map:
            #allowing the users to select their desired coffee.
            selected_coffee = MENU[choice_map[user]]
            print(f"\nDetails of {choice_map[user].replace('_', ' ')} are:")
            
            for key, value in selected_coffee.items():
                print(key,value)
            print("\n")
            amount = process_coins()
            cost = selected_coffee["cost"]
            #change is rounded to 2 decimal so that change is given at the ease.
            change = round((amount - cost),2)
            
            if change >= 0:
                print(f"Here is ${change} in change. Here is your {choice_map[user]} ☕ enjoy")
                # To Check if there are enough resources to make the selected coffee
                sufficient_resources = True
                for ingredient, content in selected_coffee["ingredients"].items():
                    if resources[ingredient] < content:
                        print(f"Sorry, not enough {ingredient} for {choice_map[user]}.")
                        sufficient_resources = False
                        break
                money = 0
                if sufficient_resources:
                    for ingredient, content in selected_coffee["ingredients"].items():
                        resources[ingredient] -= content
                    money += cost
                    resource() #This is to see what the user has paid for.
            else:
                print("Sorry, not enough money inserted. Please try again.")
        elif user == 'r':
            resource() #Reverts to normal resource def called.
                
        else:
            print("Invalid choice")
            
    user= input("\nType 'r' to view the resources to make coffee. \nWhat would you like? (espresso/latte/cappuccino): \n")
    choice_map(user)


# profit = 0
# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True


# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total


# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False


# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")


# is_on = True

# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])


# def print_report():
#
#     print("Resources remaining:")
#     for item, amount in resources.items():
#         print(f"{item} : {amount}")
#     print(f"Money : £{money:.2f}")
# def sufficient_resources(drink_choice):
#
#     for item, amount in MENU[drink_choice]['ingredients'].items():
#         if resources[item] < amount:
#             print(f"Sorry there is insufficient {item}.")
#             return False
#     return True
#
# def take_money(total_money_inserted, cost):
#     global money
#
#     money += cost
#     change = total_money_inserted - cost
#     if change > cost:
#         print(f"Here is your change, £{change:.2f}")
#     else:
#         print("Exact money given.")
#
# def sufficient_money(drink_choice):
#
#     total_money_inserted = 0
#     for coin, value in coins.items():
#         number_of_coins = int(input(f"How many {coin} added? "))
#         total_money_inserted += value * number_of_coins
#
#     total_money_inserted /= 100
#     cost = MENU[drink_choice]['cost']
#     if cost > total_money_inserted:
#         return False
#     else:
#         take_money(total_money_inserted,cost)
#         return True
#
# def make_coffee(drink_choice):
#
#     for item in MENU[drink_choice]['ingredients']:
#         resources[item] -= MENU[drink_choice]['ingredients'][item]
#
# power_on = True
# while power_on:
#     drink_choice = input("What would you like? (espresso/latte/cappuccino): ")
#     match drink_choice:
#         case 'quit':
#             print("Thank you. Powering down ..")
#             power_on = False
#         case 'report':
#             print_report()
#         case _:
#             if sufficient_resources(drink_choice):
#                 if sufficient_money(drink_choice):
#                     make_coffee(drink_choice)
#                     print(f"Enjoy your {drink_choice}")
#                 else:
#                     print("Insufficient funds. COINS RETURNED")
#             else:
#                 print(f"Sorry {drink_choice} is unavailable")
#
#
#
