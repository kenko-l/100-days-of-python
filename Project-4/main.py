from doctest import script_from_examples
from fileinput import close
import sys

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
        "cost": 1.5,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
"money": 0.0,
}


def print_report():
    """Prints the current resource values."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")

def check_resources(drink):
    """Checks if there are enough resources to make the chosen drink."""
    for item in MENU[drink]['ingredients']:
        if MENU[drink]['ingredients'][item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Handles coin input and returns the total amount inserted."""
    print("Please insert coins.")
    total = (
        int(input("How many quarters?: ")) * 0.25 +
        int(input("How many dimes?: ")) * 0.10 +
        int(input("How many nickels?: ")) * 0.05 +
        int(input("How many pennies?: ")) * 0.01
    )
    return total

def make_coffee(drink):
    """Deducts the required ingredients from the resources and makes the coffee."""
    for item in MENU[drink]['ingredients']:
        resources[item] -= MENU[drink]['ingredients'][item]
    resources['money'] += MENU[drink]['cost']
    print(f"Here is your {drink}. Enjoy!")


def coffee_machine():
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_input == "off":
            sys.exit(0)

        elif user_input == "report":
            print_report()


        elif user_input in MENU:
            if check_resources(user_input):
                print(f"That costs {MENU[user_input]['cost']}$")
                payment = process_coins()
                if payment >= MENU[user_input]['cost']:
                    change = round(payment - MENU[user_input]['cost'], 2)
                    print(f"Here is ${change} in change.")
                    make_coffee(user_input)
                else:
                    print("Sorry, that's not enough money. Money refunded.")
            else:
                continue
        else:
            print("Invalid choice. Please choose from espresso, latte, or cappuccino.")

coffee_machine()