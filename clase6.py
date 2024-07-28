import random

dictionary ={}
for i in range(1,6):
    dictionary[i] = i * 2

print(dictionary)

dictionary_v2 = {i:i*2 for i in range(1,6)}
print(dictionary_v2)

countries_list = ["Colombia", "Bolivia", "Mexico", "Peru"]
population = {}
for country in countries_list:
    population[country] = random.randint(1,100)

print(population)

population_v2 = {country: random.randint(1,100) for country in countries_list}
print(population_v2)

names_list = ["Jeronimo", "Juan Pablo", "Carolina"]
ages_list = [22, 20, 19]

names_ages_list = list(zip(names_list,ages_list))
print(names_ages_list)

names_ages_dict = {name: age for (name, age) in names_ages_list}
print(names_ages_dict)