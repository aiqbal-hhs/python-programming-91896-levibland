class Player:
    def __init__(self, _name, _first_name, _last_name, _age, _health, _diseases, _items, _weapons, _memberships):
        self.name = _name
        self.first_name = _first_name
        self.last_name = _last_name
        self.age = _age
        self.health = _health
        self.diseases = _diseases
        self.items = _items
        self.weapons = _weapons
        self.memberships = _memberships
    
    def changeName(self, _name):
        self.name = _name
    
    def changeFirstName(self, _first_name):
        self.first_name = _first_name
    
    def changeLastName(self, _last_name):
        self.last_name = _last_name
    
    def incrementAge(self):
        self.age += 1
    
    def decreaseAge(self, _amount):
        self.age -= _amount
    
    def increaseHealth(self, _amount):
        self.health += _amount
    
    def decreaseHealth(self, _amount):
        self.health -= _amount
    
    def addDisease(self, _disease):
        self.diseases.append(_disease)
    
    def removeDisease(self, _disease):
        self.diseases.remove(_disease)
    
    def addItem(self, _item, _quantity):
        self.items[item] = _quantity
    
    def removeItem(self, _item):
        del self.items[_item]
    
    def addWeapon(self, _weapon):
        self.weapons.append(_weapon)
    
    def removeWeapon(self, _weapon):
        self.weapons.remove(_weapon)
    
    def addMembership(self, _org_id):
        self.memberships.append(_org_id)

    def removeMembership(self, _org_id):
        self.memberships.remove(_org_id)
