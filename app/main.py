import utils
import read_csv
import charts


def run():
    data = read_csv.read_csv("./app/world_population.csv")

    country = input("Escribe un pais: ")
    result = utils.population_by_country(data, country)
    if len(result) > 0:
        country = result[0]
        keys, values = utils.get_population(country)
        charts.generate_bar_chart(keys, values)


def world_chart():
    data = read_csv.read_csv("./app/world_population.csv")
    key = [element.keys() for element in data]
    values = [element.values() for element in data]
    print(key)


if __name__ == "__main__":
    world_chart()
