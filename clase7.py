import random

countries_list = ["Colombia", "Bolivia", "Mexico", "Peru"]
population_v2 = {country: random.randint(1,100) for country in countries_list}
print(population_v2)

result = {country: population for (country,population) in population_v2.items() if population > 40}
print(result)

text = 'Hola, soy Juan Pablo'
unique = {c: c.upper() for c in text if c in 'aeiou'}
print(unique)