from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker_coffee = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

final_coffee = True

while final_coffee:
    option = menu.get_items()
    chose = input(f"What is coffee to place in order {option}? :").lower()
    if chose == 'off':
        final_coffee = False
    elif chose == 'report':
        maker_coffee.report()
        money.report()
    else:
        drink = menu.find_drink(chose)
        if maker_coffee.is_resource_sufficient(drink):
           if money.make_payment(drink.cost):
               maker_coffee.make_coffee(drink)



