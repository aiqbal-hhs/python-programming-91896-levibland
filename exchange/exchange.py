class Exchange:
    def __init__(self, _stocks):
        self.stocks = _stocks

    def purchase(self, _stock, _amount):
        if _stock not in list(self.stocks):
            pass
        else:
            price = self.stocks[_stock] * _amount
            print(f'You have bought {_amount} {_stock}, worth an astounding ${price}')

def main():
    stocks = {"brk.a": 419000, "bb": 15, "amc": 65, "bbby": 10, "gme": 250, "wish": 60, "clov": 40, "wkhs": 23}

    exchange = Exchange(stocks)
    
    age = int(input("How old are you> "))

    while age < 18:
        print("You must be 18 to buy stocks.\n")
        age = int(input("How old are you> "))

    for stock in list(stocks):
        print(f'{stock}\n')
    
    stock = input("Choose a stock> ").lower().strip()

    while stock not in list(stocks):
        print("That stock does not exist")
        for stock in list(stocks):
            print(f'{stock}\n')

        stock = input("Choose a stock> ").lower().strip()

    amount = float(input("Amount> "))

    while amount <= 0:
        print("You have to buy an amount greater than zero.\n")
        amount = float(input("Amount> "))

    exchange.purchase(stock, amount)


if __name__ == "__main__":
    main()
