from money_machine import MoneyMachine
from menu import Menu
from coffee_maker import CoffeeMaker

items = Menu()
maquina_dinero = MoneyMachine()
maquina_cafe = CoffeeMaker()

state = ""
while not state == "off":
    state = input(f"What coffee do you want? {items.get_items()}: ").lower()
    if state == "report":
        maquina_cafe.report()
        maquina_dinero.report()
    if state == "latte" or state == "espresso" or state == "cappuccino":
        drink = items.find_drink(state)
        if maquina_cafe.is_resource_sufficient(drink) and maquina_dinero.make_payment(drink.cost):
            maquina_cafe.make_coffee(drink)
