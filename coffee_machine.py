menu = {
    "latte": {
        "ingredient": {
            "water": 100,
            "milk": 200,
            "coffee": 50
        },
        "money": 90
    },
    "espresso": {
        "ingredient": {
            "water": 100,
            "milk": 100,
            "coffee": 70
        },
        "money": 140
    },
    "cappuccino": {
        "ingredient": {
            "water": 200,
            "milk": 200,
            "coffee": 80
        },
        "money": 195
    }

}

resource = {
    "water": 1000,
    "milk": 1000,
    "coffee": 500
}


def check_coin():
    global amount
    rs5 = int(input("How many 5 Rs coin : "))
    rs10 = int(input("How many 10 Rs coin : "))
    rs20 = int(input("How many 20 Rs coin : "))
    total = rs5*5 + rs10*10 + rs20*20
    if total >= menu[customer]["money"]:
        refund = total - menu[customer]["money"]
        amount += menu[customer]["money"]
        print(f"Here is your change {refund}")
        return True
    else:
        print(f"You Did Not Entered Enough Money....\nHere's Your Money {total}")
        return False


def have_resouce():
    for quantity in menu[customer]["ingredient"].keys():
        for have_quantity in resource.keys():
            if menu[customer]["ingredient"][quantity] <= resource[have_quantity]:
                return True
            else:
                print(f"We don't have enough {quantity} ")
                return False


def make_coffee(customer_choice):
    for choice in resource.keys():
        resource[choice] -= menu[customer_choice]["ingredient"][choice]
    print(f"Here's Your {customer_choice}...\nPlease Enjoy It...")


amount = 0
machine_on = True
while machine_on:
    customer = input("What would you like to have (Latte/Espresso/Cappuccino) : ").lower()
    count = 0
    if customer == "off":
        machine_on = False
    elif customer == "report":
        for item, value in resource.items():
            print(f"{item.upper()} : {value}")
        print(f"money : {amount}")
    elif customer in menu.keys():
        if have_resouce():
            if check_coin():
                make_coffee(customer)
            else:
                print("Please Try Again....\n")
    else:
        print("Sorry.....\nYou Entered something wrong.... \nPlease Try Again With Right Choice.....\n")
        continue
