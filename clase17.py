items = [
    {
        'product':'Camisa',
        'price':100
    },
    {
        'product':'buzo',
        'price':200
    },
    {
        'product':'pantalones',
        'price':250
    },
    {
        'product':'medias',
        'price':50
    }
]

items2 = [
    {
        'product':'Camisa',
        'price':100
    }
]

prices = list(map(lambda product: product,items2))
def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item

items_with_taxes_list = list(map(add_taxes,items2))
keys = [key for item in items_with_taxes_list for key in item.keys()]
values = [key for item in items_with_taxes_list for key in item.values()]
print(values)
print(keys)
iterable = zip(keys,values)
product_dict = {key:value for key, value in iterable}
print(product_dict)
print(items_with_taxes_list)
