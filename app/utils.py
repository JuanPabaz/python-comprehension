def get_population():
    keys = ["Colombia", "Bolivia"]
    values =[ 50,30]
    return keys,values

def population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result