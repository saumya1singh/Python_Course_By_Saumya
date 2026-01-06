MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0
    }
}


resources = {
    "water": 500,
    "milk": 400,
    "coffee": 300,
    "money": 0
}

def check_resources(drink):
    for item in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][item] > resources.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total

def transaction_successful(drink, money_received):
    cost = MENU[drink]["cost"]
    if money_received < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = round(money_received - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        resources["money"] += cost
        return True

def make_coffee(drink):
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    print(f"Here is your {drink}. Enjoy!")


def coffee_machine():
    is_on = True
    while is_on:
        choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            print("Turning off the coffee machine... Goodbye!")
            is_on = False
        elif choice == "report":
            report()
        elif choice in MENU:
            if check_resources(choice):
                payment = process_coins()
                if transaction_successful(choice, payment):
                    make_coffee(choice)
        else:
            print("Invalid choice. Please select espresso, latte, or cappuccino.")

