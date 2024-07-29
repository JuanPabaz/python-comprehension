import csv


def read_csv(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        data = []
        header = [
            element for element in header if element == "World Population Percentage"
        ]
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data


if __name__ == "__main__":
    data = read_csv("./app/world_population.csv")
    print(data)
