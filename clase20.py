# Reduce(fun, seq) tiene dos parametros:

# Una función particular a aplicar a todos los elementos de una secuencia
# Una secuencia de elementos.
# Como funciona:

# Primero toma los dos primeros elementos de la secuencia y aplica la función particular.
# Toma el resultado anterior y a este valor mas el siguiente elemento de la secuencia le aplica la función particular.
# El proceso continua hasta que no tiene mas elementos.
# Retorna el resultado.

import functools
numbers = [4,5,6,7]

def accum(x,y):
    print(x)
    print(y)
    return x,y


numbers_reduce = functools.reduce(lambda x,y: x + y, numbers)
print(numbers_reduce)