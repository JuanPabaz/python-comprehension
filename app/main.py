import utils

country, population = utils.get_population()
print(country,population)

data = [
    {
        'Country':'Colombia',
        'Population':50
    },
    {
        'Country':'Bolivia',
        'Population':30
    }
]

country = input('Escribe un pais: ')
result = utils.population_by_country(data,country)
print(result)