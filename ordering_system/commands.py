###  COMMANDS FILE  ###

from orderbook import Orderbook

# @notice the commands function
# @param _orderbook the pizza orderbook used in main
def commands(_orderbook: Orderbook):
    print('Enter a command, or type `help` for help.\n')

    running: bool = True

    while running:
        command: str = input('> ')
        formatted: str = command.lower().strip()

        if formatted == ('help'):
            print('Here are the possible commands: new<start a new order>, pay<pay for a completed order>, quit<to quit>, help<get help>\n')

        elif formatted == ('new'):
            pizzas: list = _orderbook.get_pizzas()

            print('Possible Pizzas:\t\tNumber\t\tName\t\t\tPrice')
            for i in range(len(pizzas)):
                print(f'({i})\t\t{pizzas[i].get_name()}\t\t\t${pizzas[i].get_price()}')
