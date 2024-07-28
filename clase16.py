#Map = MAP( ) La función map () ejecuta una función especifica para cada elemento 
#en un iterable y el elemento se envía a la función como un parámetro.
#Sintaxis = map(function, iterables)

numbers = [1,2,3,4,5]
numbers_v2 = []

for number in numbers:
    numbers_v2.append(number*2)

print(numbers_v2)
print(numbers)

numbers_v3 = list(map(lambda number: number * 2, numbers))

print(numbers_v3)

numbers_v4 = [1,2,3,4]
numbers_v5 = [5,6,7]

print(numbers_v4)
print(numbers_v5)
#La listas tienen diferentes tamaños, por lo que el tamaño de la lista 
#resultante es el de la lista mas pequeña
result = list(map(lambda x, y: x + y, numbers_v4, numbers_v5))
print(result)