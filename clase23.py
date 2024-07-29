try:
    print(0/0)
    x = 10
    if x < 18:
        raise Exception('No se permiten menores de edad')
    assert 1 != 1, 'Uno no es igual que uno'
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)


print("Hola")