import random

class World:
    def __init__(self, _players, _date, _gangs, _popo):
        self.players = _players
        self.date = _date
        self.gangs = _gangs
        self.popo = _popo
        self.current_uuid = 1
        self.current_gang_id = 1
        self.cemetery = {}
        self.gang_ids = []

    def birth(self, _player_data):
        self.players[self.current_uuid] = _player_data
        self.current_uuid += 1
        print(f"{_player_data.name} has been born.\n")
    
    def kill(self, _uuid, _reason):
        player_data = self.players[_uuid]
        del self.players[_uuid]
        self.cemetery[_uuid] = player_data
        print(f'{player_data.name} has died of {_reason}.\n')
    
    def incrementYear(self):
        self.date += 1

    def removeGang(self, _gang_id):
        print(f'{self.gangs[_gang_id].name} has no members and is now defunct.\n')
        del self.gangs[_gang_id]
        self.gang_ids.remove(_gang_id)

    def addGang(self, _gang_data):
        self.gangs[self.current_gang_id] = _gang_data
        self.gang_ids.append(self.current_gang_id)
        print(f'{self.gangs[self.current_gang_id].name} has been formed by {self.players[self.gangs[self.current_gang_id].leader].name}.\n')
        self.current_gang_id += 1
    
    def attack(self, _gang_id_1, _gang_id_2):
        print(f'{self.gangs[_gang_id_1].name} has attacked {self.gangs[_gang_id_2].name}.\n')

        for member in range(len(self.gangs[_gang_id_1].members)):
            rnd = random.randint(0, 10)
            rnd2 = random.randint(0, 5)
            health_decrease = int(rnd * rnd2)

            self.players[self.gangs[_gang_id_1].members[member]].decreaseHealth(health_decrease)
            
            print(f'{self.players[self.gangs[_gang_id_1].members[member]].name} has had their skull smashed in the brawl with {self.gangs[_gang_id_2].name}, losing {health_decrease} health.\n')
        
        for member in range(0, len(self.gangs[_gang_id_2].members)):
            rnd = random.randint(0, 10)
            rnd2 = random.randint(0, 5)
            health_decrease = rnd * rnd2

            self.players[self.gangs[_gang_id_2].members[member]].decreaseHealth(health_decrease)
            print(f'{self.players[self.gangs[_gang_id_2].members[member]].name} has had their skull smashed in the brawl with {self.gangs[_gang_id_1].name}, losing {health_decrease} health.\n')
            
    def attack_popo(self, _gang_id):
        print(f'{self.gangs[_gang_id].name} has attacked the police.\n')

        for member in range(len(self.gangs[_gang_id].members)):
            rnd = random.randint(1, 2)

            health_decrease = int(100 / rnd)
            self.players[self.gangs[_gang_id].members[member]].decreaseHealth(health_decrease)
            print(f'{self.players[self.gangs[_gang_id].members[member]].name} has been shot by the Police, losing {health_decrease} health.\n')
        
        for officer in range(len(self.popo.members)):
            rnd = random.randint(0, 5)
            rnd *= random.randint(0, 10)

            self.players[self.popo.members[officer]].decreaseHealth(rnd)
            print(f'{self.players[self.popo.members[officer]].name} has been smashed with a club during the fight with {self.gangs[_gang_id].name}, losing {rnd} health.\n')
    
    def popo_raid(self, _gang_id):
        print(f'The police have raided {self.gangs[_gang_id].name}.\n')
        for member in range(len(self.gangs[_gang_id].members)):
            rnd = random.randint(1, 2)

            health_decrease = int(100 / rnd)
            self.players[self.gangs[_gang_id].members[member]].decreaseHealth(health_decrease)
            print(f'{self.players[self.gangs[_gang_id].members[member]].name} has been shot by the Police, losing {health_decrease} health.\n')
        
        for officer in range(len(self.popo.members)):
            rnd = random.randint(0, 5)
            rnd *= random.randint(0, 10)

            self.players[self.popo.members[officer]].decreaseHealth(rnd)
            print(f'{self.players[self.popo.members[officer]].name} has been smashed with a club during the fight with {self.gangs[_gang_id].name}, losing {rnd} health.\n')
