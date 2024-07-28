set_countries = {'Colombia', 'Mexico', 'Bolivia','Colombia'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 3, 4, 2}
print(set_numbers)

set_types = {1, "Hola", False, 2.34}
print(set_types)

set_from_string = set('Hooolaaaa')
print(set_from_string)

set_from_tupla = set((1,24,3,5,'abc',2.34))
print(set_from_tupla)

numbers = [1,3,2,4,1,2,3,4]
set_from_list = set(numbers)
print(set_from_list)

unique_numbers = list(set_from_list)
print(unique_numbers)