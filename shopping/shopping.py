# shopping program

balance = 100

still_shopping = True
ticker = 0

while balance > 0:
    if ticker > 0:
        uin = input("Do you want to continue shopping, yes/no?\n")
    else:
        uin = input("Do you want to go shopping?\n")
    if uin.lower().strip() == ("yes"):
        item_to_buy = input("What do you want to buy?\n")
        price = float(input("What is your items price?\n"))
        if price > balance:
            print(f"You do not have enough money to buy {item_to_buy} for {price}.\n")
            ticker = 1
        else:    
            balance -= price
            items = {}
            items[item_to_buy] = price
            print(f"You have bought {item_to_buy} for the price of {price}.\n")
            print("Here are your items and their prices:\n")
            print(items)
            ticker = 1
            
    elif uin.lower().strip() == ("no"):
        print(f"You have chosen to stop shopping.\n")
        print(items)
        balance = 0
