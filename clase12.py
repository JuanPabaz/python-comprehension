price = 100 #Global

def increment_value():
    price = 200
    result = price + 10
    print(result)
    return result

print(price)
result = increment_value()
print(result)