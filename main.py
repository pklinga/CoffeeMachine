MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


def print_resources():
    print(water_left)
    print(milk_left)
    print(coffee_left)
    print(f"Money: ${money_in_machine}")


def check_resources_sufficiency(water, milk, coffee):
    """Returns True if all resources are available, and False if not."""
    if water_left < water:
        print("There is not enough water left.")
        return False
    elif milk_left < milk:
        print("There is not enough milk left.")
        return False
    elif coffee_left < coffee:
        print("There is not enough coffee left.")
        return False
    else:
        return True


def process_coins():
    """Returns the coins inserted."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    inserted_coins = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return inserted_coins


machine_off = False
money_in_machine = float(0)
water_left = resources["water"]
milk_left = resources["milk"]
coffee_left = resources["coffee"]


while not machine_off:
    wanted_coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if wanted_coffee != "off":
        if wanted_coffee == "report":
            print_resources()
        else:
            if check_resources_sufficiency(MENU[wanted_coffee]["ingredients"]["water"], MENU[wanted_coffee][
                                          "ingredients"]["milk"], MENU[wanted_coffee]["ingredients"]["coffee"]):
                payment = process_coins()
                if payment >= MENU[wanted_coffee]["cost"]:
                    change_back = round(payment - MENU[wanted_coffee]["cost"], 2)
                    print(f'Here is your change: ${change_back}.')
                    water_left -= MENU[wanted_coffee]["ingredients"]["water"]
                    milk_left -= MENU[wanted_coffee]["ingredients"]["milk"]
                    coffee_left -= MENU[wanted_coffee]["ingredients"]["coffee"]
                    money_in_machine += MENU[wanted_coffee]["cost"]
                    print(f"Here is your {wanted_coffee}. ☕ Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
    else:
        machine_off = True
