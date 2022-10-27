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


def print_resource_report():
    """Prints a report of the current amounts of available resources."""
    total_water = resources["water"]
    total_milk = resources["milk"]
    total_coffee = resources["coffee"]
    print(f"Water: {total_water}ml")
    print(f"Milk: {total_milk}ml")
    print(f"Coffee: {total_coffee}g")
    profit = "{:.2f}".format(total_profit)
    print(f"Money: ${profit}")


def enough_ingredients(drink_ingredients):
    """Returns 'True' if there are enough ingredients to make requested drink,
    else returns 'False'."""
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def make_drink(drink_selection):
    """Makes the requested drink and updates the resources available."""
    ingredients = MENU[drink_selection]["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]


def prompt_user():
    """Prompts user for item to order or action to perform."""
    return input("What would you like? (espresso/latte/cappuccino): ").lower()


def update_total_profit(total, drink_price):
    """Returns the updated total profit."""
    total += drink_price
    return total


def process_coins(drink_price):
    """Calculates if the amount given in coins is enough to pay for the coffee.
    Returns the amount of change or will cancel transaction if insufficient funds."""
    total_payed = 0.00
    quarters_inserted = int(input("How many quarters?: "))
    dimes_inserted = int(input("How many dimes?: "))
    nickels_inserted = int(input("How many nickels?: "))
    pennies_inserted = int(input("How many pennies?: "))

    # Total the amount received in coins
    for coin in range(1, quarters_inserted + 1):
        total_payed += 0.25
    for coin in range(1, dimes_inserted + 1):
        total_payed += 0.10
    for coin in range(1, nickels_inserted + 1):
        total_payed += 0.05
    for coin in range(1, pennies_inserted + 1):
        total_payed += 0.01

    # format 'total_payed' to 2 decimal points
    total_payed = float("{:.2f}".format(total_payed))

    # total payment is enough, return change if any
    if total_payed >= drink_price:
        change = "{:.2f}".format(total_payed - drink_price)
        print(f"Your change is: ${change}")
        return True
    else:
        print("Sorry you do not have enough for that drink. Money refunded.")
        return False


# Flag representing if the coffee program should terminate
end_program = False
total_profit = 0.0

# while coffee machine has not been turned off...
while not end_program:
    total_bill = 0.0
    selection = prompt_user()

    # print report of available resources/ingredients
    if selection == "report":
        print_resource_report()

    # user selected a coffee, check to see if there are enough ingredients,
    # charge the customer and handle the transaction
    elif selection == "espresso" or selection == "latte" or selection == "cappuccino":
        if enough_ingredients(MENU[selection]["ingredients"]):
            total_bill = MENU[selection]["cost"]
            print("Please insert coins: ")
            transaction_successful = process_coins(total_bill)
            if transaction_successful:
                total_profit = update_total_profit(total_profit, total_bill)
                make_drink(selection)
                print(f"Here is your {selection}. Enjoy!")

    # user selected to turn the coffee machine off, terminates program
    elif selection == "off":
        end_program = True

    # user selected an invalid option
    else:
        print("Sorry. Invalid option.")

