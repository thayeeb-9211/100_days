from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffee_machine():
    coffee_maker = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()

    while True:
        options = menu.get_items()
        user_input = input(f"What would you like? ({options}): ").lower()

        if user_input == 'off':
            print("Turning off the coffee machine...")
            break
        elif user_input == 'r':
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(user_input)
            if drink is None:
                print("Invalid option. Please try again.")
                continue

            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
coffee_machine()
