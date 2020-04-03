#! python3

names = ['Bruce', 'Peter', 'Logan']
heros = ['Batman', 'Spiderman', 'Wolverine']
print(dict(zip(names, heros)))

# I want dict{‘name’: ‘hero’} for each name, hero in zip(names, heros)
myDict = {}
for name, hero in zip(names, heros):
    myDict[name] = hero
print(myDict)

# dictionary comprehension
myDict = {name: hero for name, hero in zip(names, heros)}
print(myDict)
