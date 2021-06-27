from world import World
from player import Player
from gangs import Gang
from police import Police

import random
import pickle
import names
import diseases

turn_number = 0

world = World({0: Player("Genesis", "Genesis", "", 0, 1000, [], [], ["Club"], [])}, 2100, {}, Police([], ""))

def start_screen():
    print("Type play to start.\n")
    selection = input('> ')
    first_name = input('Your first name> ')
    last_name = input('Your last name> ')
    name = first_name + ' ' + last_name
    player = Player(name, first_name, last_name, 0, 100, [], [], [], [])
    world.players[-1] = player
    print(f'{name} has been born.\n')

    while selection.lower().strip() != ('play'):
        print("Type play to start.\n")
        selection = input('> ')
        first_name = input('Your first name> ')
        last_name = input('Your last name> ')
        name = first_name + ' ' + last_name
        player = Player(name, first_name, last_name, 0, 100, [], [], [], [])
        world.players[-1] = player
        print(f'{name} has been born.\n')
    

def populationControl():
    dead_players = []
    rnd = random.randint(0, 100)

    for i in range(int(rnd / 20)):
        if rnd > 30:
            first_name = random.choice(names.first_names)
            last_name = random.choice(names.last_names)
            name = first_name + ' ' + last_name
            age = 0
            health = 100
            diseases_list = []

            if rnd > 9:
                disease = random.choice(diseases.diseases)
                diseases_list.append(disease)

            items = []
            weapons = ["Club"]
            new_player = Player(name, first_name, last_name, age, health, diseases_list, items, weapons, [])

            world.birth(new_player)

    for player in world.players:
        try:
            world.players[player].incrementAge()
        except KeyError:
            pass
    
    for player in world.players:
        rnd = random.randint(0, 100)
        if world.players[player].age > 75 and rnd > 90:
            dead_players.append(player)
        
        if world.players[player].health <= 0:
            print(f'{world.players[player].name} has died of their injuries.\n')
            dead_players.append(player)
    
    for i in range(len(dead_players)):
        for membership in world.players[dead_players[i]].memberships:
            world.gangs[membership].removeMember(dead_players[i])
        world.kill(dead_players[i], 'old age')


def gangControl():
    rnd = random.randint(0, 10)
    running = 0
    
    if rnd > 9:
        
        founder = random.choice(list(world.players))
        while founder == -1:
            founder = random.choice(list(world.players))

        while world.players[founder].age < 13 and running < 10:
            founder = random.choice(list(world.players))
            if len(world.players[founder].memberships) > 0:
                founder = random.choice(list(world.players))
                pass
            running += 1
        
        if world.players[founder].age >= 13:
            name1 = random.choice(names.gang_names)
            name2 = random.choice(names.gang_names)
            name = name1 + ' ' + name2

            street_name = random.choice(names.street_names)
            street_suffix = random.choice(names.street_suffixes)
            address_number = random.randint(1, 10000)

            street = str(address_number) + ' ' + street_name + ' ' + street_suffix

            gang = Gang(name, founder, [founder], street)
            world.players[founder].addMembership(world.current_gang_id)
            world.addGang(gang)
    
    elif rnd < 2 and len(world.gang_ids) > 0:
        gang = random.choice(world.gang_ids)
        player = random.choice(list(world.players))
        while player == -1:
            player = random.choice(list(world.players))
        
        name = world.players[player].name

        while len(world.players[player].memberships) > 0:
            player = random.choice(list(world.players))

        if world.players[player].age >= 13:
            world.gangs[gang].addMember(player, name)
            world.players[player].addMembership(gang)
    
    for gang in world.gang_ids:
        if len(world.gangs[gang].members) == 0:
            world.removeGang(gang)
            break
    
    rnd = random.randint(0, 10)

    if rnd > 8:
        if len(world.gang_ids) >= 2:
            gang1 = random.choice(world.gang_ids)
            gang2 = random.choice(world.gang_ids)
            while gang1 == gang2 or gang1 == -1 or gang2 == -1:
                gang1 == random.choice(world.gang_ids)
                gang2 = random.choice(world.gang_ids)
            
            world.attack(gang1, gang2)
        else:
            pass
    
    elif rnd == 5:
        if len(world.gang_ids) > 0:
            gang = random.choice(world.gang_ids)
            while gang == -1:
                gang = random.choice(world.gang_ids)

            world.attack_popo(gang)
        else:
            pass

    elif rnd == 6:
        if len(world.gang_ids) > 0:
            gang = random.choice(world.gang_ids)

            world.popo_raid(gang)

def gameloop():
    running = True

    start_screen()

    while running:
        commands()
        populationControl()
        gangControl()

def commands():
    command = input('> ')

    formatted = command.lower().strip()

    if formatted == ('help'):
        print('List of commands: help, attack, steal.\n')
    elif formatted == ('inquire'):
        target = int(input('Target\'s uuid: '))
        print(world.players[target].name)
        print(world.players[target].first_name)
        print(world.players[target].last_name)
        print(world.players[target].age)
        print(world.players[target].health)
        print(world.players[target].diseases)
        print(world.players[target].items)
        print(world.players[target].weapons)
        print(world.players[target].memberships)
    elif formatted == ('list'):
        for player in world.players:
            print(f'uuid: {player}, name: {world.players[player].name}')
    elif formatted == ('listgangs'):
        for gang in world.gangs:
            print(f'gang_id: {gang}, name: {world.gangs[gang].name}')
    elif formatted == ('ganginquiry'):
        target = int(input('Target gang\'s id: '))
        print(world.gangs[target].name)
        print(world.gangs[target].leader)
        print(world.gangs[target].members)
        print(world.gangs[target].address)
    elif formatted == ('cem'):
        for deceased in world.cemetery:
            print(f'uuid: {deceased}, name: {world.cemetery[deceased].name}')
    elif formatted == ('ceminquiry'):
        target = int(input('Target\'s uuid: '))
        print(world.cemetery[target].name)
        print(world.cemetery[target].first_name)
        print(world.cemetery[target].last_name)
        print(world.cemetery[target].age)
        print(world.cemetery[target].health)
        print(world.cemetery[target].diseases)
        print(world.cemetery[target].items)
        print(world.cemetery[target].weapons)
        print(world.cemetery[target].memberships)
    elif formatted == ('form'):
        if len(world.players[-1].memberships) > 0:
            pass
        else:
            name = input('New gang\'s name> ')
            street_name = random.choice(names.street_names)
            street_suffix = random.choice(names.street_suffixes)
            address_number = random.randint(1, 10000)
            street = str(address_number) + ' ' + street_name + ' ' + street_suffix
            founder = -1

            gang = Gang(name, founder, [founder], street)
            world.gangs[-1] = gang
            print(f'{name} has been formed by {world.players[founder].name}.\n')
    elif formatted == ('attack'):
        target = int(input('Target gang> '))
        while target == -1:
            print('You can\'t attack your own gang, try again.\n')
            target = int(input('Target gang> '))
        world.attack(-1, target)

    else:
        pass

def main():
    gameloop()
    

if __name__ == '__main__':
    main()
