# Branching program
import random

name = input("Your name: ")
rnd = random.random() * 10

if rnd > 2:
    print(f'I hate you {name}')

elif rnd < 8 and rnd > 2:
    print(f'I hate you so much')

