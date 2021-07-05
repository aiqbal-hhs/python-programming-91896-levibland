###  PIZZA ORDERING SYSTEM  ###

from pizza import Pizza

import constants

# @notice orderbook ordering system
class Orderbook:
    # @notice constructs the orderbook class
    def __init__(self, _pizzas: dict[int, Pizza], _current_pizza_id: int):
        self.pizzas = _pizzas
        self.current_pizza_id = _current_pizza_id
    
    # @notice orders pizzas
    # @param _pizza_ids the list of pizzas to be ordered
    # @param _amounts the list of amounts of pizzas to be ordered
    def order(self, _pizza_ids: list[int], _amounts: list[int]):
        total = self.total(_pizza_ids, _amounts)
        print('======================================================')
        print('====================  Your Order  ====================')
        print('======================================================')
        print('Item No.     Name                    Amount      Price')

        for i in range(len(_pizza_ids)):
            print(f'\t({i})\t\t{self.pizzas[_pizza_ids[i]].get_name()}\t\t\t\t\t{_amounts[i]}\t\t${self.pizzas[_pizza_ids[i]].get_price()}\n')
        
        print('======================================================')
        print('=======================  Total  ======================')
        print('======================================================')
        print(f'TOTAL(including $3.00 delivery fee): {total}')
    
    # @notice returns the total of an order
    # @param _pizza_ids the list of ordered pizzas
    # @param _amounts the amount of each pizza to order
    # @return total the total cost of all pizzas combined
    def total(self, _pizza_ids: list[int], _amounts: list[int]) -> float:
        total: float = float(0)

        for i in range(len(_pizza_ids)):
            price: float = self.pizzas[_pizza_ids[i]].get_price()
            total += price

        total += constants.DELIVERY_FEE

        return total
    
    # @notice adds a pizza
    # @param _new_pizza the pizza to add
    def add_pizza(self, _new_pizza: Pizza):
        self.pizzas[self.current_pizza_id] = _new_pizza

        self.current_pizza_id += 1
    
    # @notice removes a pizza
    # @param _pizza_id the id of the pizza to remove
    def remove_pizza(self, _pizza_id: int):
        del self.pizzas[_pizza_id]

    # @notice gets all the possible pizzas
    # @return pizzas all the possible pizzas
    def get_pizzas(self) -> list[Pizza]:
        pizzas: list = []

        for i in range(len(list(self.pizzas))):
            pizzas.append(self.pizzas[i])
        
        return pizzas
