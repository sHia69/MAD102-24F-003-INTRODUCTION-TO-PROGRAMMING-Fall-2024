# Question 14
# Purpose: B. Develop a Python program to register k players for a gaming tournament and generates Player Tag. Program should collect information from user such as Player Name, Game Type, and Age and generate a Player Tag in the format: “GameType-Age-First 2 letters of Player Name-Random Number between 500 and 999”. Print the Player Tag for each participant.

import random

tags = []

while True:
    name = input('Enter Player Name:')
    if len(name) < 2:
        print('Invalid name')
        continue
    game_type = input('Enter Game Type:')
    age = input('Enter Age:')
    try:
        age = int(age)
        if age < 0:
            raise ValueError()
    except ValueError:
        print(f'Invalid age: {age!r}')
        continue
    tags.append(f'{game_type}-{age}-{name[:2]}-{random.randint(500, 999)}')
    if input('Would you like to register? ') == 'no':
        break

print('\n'.join(tags))
