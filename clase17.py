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

prices = list(map(lambda product: product['price'],items2))
print(prices)
def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item

items_with_taxes_list = list(map(add_taxes,items2))
print(items_with_taxes_list)
items_with_taxes_dict = dict(items_with_taxes_list)
print(items_with_taxes_dict)