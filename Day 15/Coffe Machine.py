
def money():
    """Return money in dollars, this is important to pay"""
    print("Please insert coins.")
    total_money= int(input("How many quarters? ") ) *0.25
    total_money += int(input("How many dimes? ") ) *0.1
    total_money += int(input("How many nickles? ") ) *0.05
    total_money += int(input("How many pennies? ") ) *0.01
    return total_money


def choosing_coffee(tipo):
    global recipe, machine_state
    i = 0
    for ingredients in ["Water", "Coffee", "Milk"]:
        if machine_state[ingredients][0] <= recipe[tipo][i]:
            print(f"Sorry there is not enough {ingredients}\n")
            return False
        i += 1
    return True


def buying(ingr_confirm, tipo):
    dinero = 0
    i=0
    global recipe, machine_state
    if not ingr_confirm:
        return
    dinero = money()
    if dinero < recipe[tipo][3]:
        print(f"Sorry that's not enough money. Money refunded.\n")
        return
    # elif (dinero-recipe[tipo][3]) > machine_state["Money"][0]:
    #    print(f"Sorry, not enough money to make change. Money refunded.")
    #    return
    else:
        for ingredients in ["Water", "Coffee", "Milk"]:
            machine_state[ingredients][0] -= recipe[tipo][i]
            i += 1
        machine_state["Money"][0] += recipe[tipo][3]
        print(f"Here is ${round(dinero-recipe[tipo][3],2)}\nPlease remove the coffee and Enjoy!\n")


machine_state = {"Water": [300, "ml"], "Milk": [200, "ml"], "Coffee": [100, "g"], "Money": [10, "$"]}
recipe = {"expresso": [50, 18, 0, 1.5], "latte": [200, 24, 150, 2.5], "cappuccino": [250, 24, 100, 3.0]}
state = "on"
while not state == "off":
    state = input("What ☕ would you like? (expresso/cappuccino/latte): ").lower()
    if state == "expresso" or state == "cappuccino" or state == "latte":
        buying(choosing_coffee(state), state)

    elif state == "report":
        for x in machine_state.keys():
            print(f"{x}: {machine_state[x][0]}{machine_state[x][1]}\n")
print("Shutting down... ")

