import json

import enchant
import re

d = enchant.request_pwl_dict('dogs.txt')
with open('animals.json') as f:
    animals = json.loads(f.read())


print(animals)

with open('dogs.txt') as f:
    dogs = f.readlines()

possibilities = dogs.copy()

for animal in animals:
    animal_lower = animal.lower()

    for possibility in possibilities:
        if animal_lower in dog:
            ret = possibility.replace(animal, '')
            possibilities.append(ret)

for possibility in possibilities:
    if 'ber' in possibility:
        print(possibility)
