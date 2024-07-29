import utils

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

def run():
    country, population = utils.get_population()
    print(country,population)

    country = input('Escribe un pais: ')
    result = utils.population_by_country(data,country)
    print(result)

if __name__ == '__main__':
    run()