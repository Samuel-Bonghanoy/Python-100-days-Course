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

def report(order, money):
    if order == "report":
        for resource in resources:
            if resource == "water" or resource == "milk":
                print(f"{resource}: {resources[resource]}ml")
            elif resource == "coffee":
                print(f"{resource}: {resources[resource]}g")
        print(f"Money: ${round(money, 1)}")

def resource_check(order):
    if order == "espresso":
        for resource in resources:
            for ingredient in MENU[order]["ingredients"]:
                if resource == ingredient:
                    if resources[resource] - MENU[order]["ingredients"][ingredient] < 0:
                        print(f"Sorry there is not enough {resource}.")
                        return False
                    else:
                        resources[resource] -= MENU[order]["ingredients"][ingredient]
                        # print(resources[resource])
        return True

    elif order == "latte":
        for resource in resources:
            for ingredient in MENU[order]["ingredients"]:
                if resource == ingredient:
                    if resources[resource] - MENU[order]["ingredients"][ingredient] < 0:
                        print(f"Sorry there is not enough {resource}.")
                        return False
                    else:
                        resources[resource] -= MENU[order]["ingredients"][ingredient]
                        # print(resources[resource])
        return True

    elif order == "cappuccino":
        for resource in resources:
            for ingredient in MENU[order]["ingredients"]:
                if resource == ingredient:
                    if resources[resource] - MENU[order]["ingredients"][ingredient] < 0:
                        print(f"Sorry there is not enough {resource}.")
                        return False
                    else:
                        resources[resource] -= MENU[order]["ingredients"][ingredient]
                        # print(resources[resource])
        return True

    elif order == "report":
        return False

def payment(order, money):
    machine_money = 0
    change = 0
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many quarters?: "))
    nickels = int(input("How many quarters?: "))
    pennies = int(input("How many quarters?: "))

    money += ((0.25 * quarters) + (0.1 * dimes) + (0.05 * nickels) + (0.01 * pennies))
    if money - (MENU[order]["cost"])< 0:
        print("Sorry, you did not insert enough money.")
        change = money
        print(f"Here is your refund of ${round(change, 2)}.")
        return machine_money
    elif money - (MENU[order]["cost"]) >= 0:
        machine_money += (MENU[order]["cost"]) 
        change = money - machine_money
        print(f"Here is ${round(change, 2)} in change.")
        print(f"Here is your {order}. Enjoy!")
        return machine_money

def c_machine():
    money = 0
    machine_money = 0

    order_in_progress = True
    
    while order_in_progress:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if order == 'off':
            order_in_progress = False
            print("Thank you for ordering!")
            return

        r_check = resource_check(order)
        report(order, machine_money)

        if r_check:
            machine_money = payment(order, money)

c_machine()


