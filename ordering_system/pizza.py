###  PIZZA CLASS IMPLEMENTATION  ###

# @notice pizza class
class Pizza:
    # @notice constructs the pizza class
    # @param _name the name of the pizza
    # @param _price the price of the pizza
    def __init__(self, _name: str, _price: float):
        self.name = _name
        self.price = _price
    
    # @notice updates this pizza's name
    # @param _new_name the name to change to
    def update_name(self, _new_name: str):
        self.name = _new_name
    
    # @notice updates this pizza's price
    # @param _new_price the cost to change to
    def update_price(self, _new_price: float):
        self.price = _new_price
    
    # @notice gets this pizza's name
    # @return the name of this pizza
    def get_name(self) -> str:
        return self.name
    
    # @notice gets this pizza's price
    # @return the price of this pizza
    def get_price(self) -> float:
        return self.price
