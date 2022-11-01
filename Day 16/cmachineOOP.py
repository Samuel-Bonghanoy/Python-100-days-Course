from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffee_machine():
    is_ordering =  True

    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    menu = Menu()

    while is_ordering:

        options = menu.get_items()
        order = input("What would you like? {options}: ").lower()

        if order == "off":
            is_ordering =  False
            return
        elif order == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = Menu.find_drink(order)

            enough_resources = coffee_maker.is_resource_sufficient(drink)

            if enough_resources:
                coffee_maker.make_coffee(MenuItem)
                payment_accepted = money_machine.make_payment(drink)

coffee_machine()
