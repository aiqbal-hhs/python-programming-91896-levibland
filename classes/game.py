class World:
  def __init__(self, _dimensions, _date):
    self.dimensions = _dimensions
    self.date = _date
    self.uuid = 0
  
  def incrementYear(self):
    self.date += 1
  
  def transfer_player(self, _uuid, _from_dimension_id, _to_dimension_id):
    player_data = self.dimensions[_from_dimension_id].players[_uuid]
    del self.dimensions.players[_uuid]
    
    self.dimensions[_to_dimension_id].players[_uuid] = player_data

class Dimension:
  def __init__(self, _players, _name, _params, _graveyard):
    self.players = _players
    self.name = _name
    self.params = _params
    self.graveyard = _graveyard
  
  def birth(self, _player_data, _current_uuid):
    self.players[_current_uuid] = _player_data
    print(f"{self.players[_current_uuid].name} has been born in the {self.name} dimension\n")
  
  def kill(self, _uuid):
    player_data = self.players[_uuid]
    del self.players[_uuid]
    self.graveyard.append(player_data)
  
class Player:
  def __init__(self, _name, _first_name, _last_name, _age, _health, _diseases, _items, _weapons, _parents):
    self.name = _name
    self.first_name = _first_name
    self.last_name = _last_name
    self.age = _age
    self.health = _health
    self.diseases = _diseases
    self.items = _items
    self.weapons = _weapons
    self.parents = _parents
  
  def incrementAge(self):
    self.age += 1
  
  def decrementAge(self):
    self.age -= 1

  def changeName(self, _new_name):
    self.name = _new_name
  
  def changeLastName(self, _new_last_name):
    self.last_name = _new_last_name
  
  def changeFirstName(self, _new_first_name):
    self.first_name = _new_first_name
  
  def increaseHealth(self, _amount):
    self.health += _amount

  def decreaseHealth(self, _amount):
    self.health -= _amount
  
  def addDisease(self, _disease):
    self.diseases.append(_disease)
  
  def removeDisease(self, _disease):
    self.diseases.remove(_disease)
