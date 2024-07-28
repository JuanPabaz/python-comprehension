def increment(x):
    return x + 1

def higer_order_funct(x, func):
    return x + func(x)

result = higer_order_funct(2, increment)#No se ejecuta, solo se envia
print(result)

increment_value = lambda x : x + 1
higer_order_funct_v2 = lambda x, func: x + func(x)
result_v2 = higer_order_funct_v2(2,increment_value)
print(result_v2)
result_v2 = higer_order_funct_v2(2,lambda x : x + 2)
print(result_v2)