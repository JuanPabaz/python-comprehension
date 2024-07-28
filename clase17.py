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

prices = list(map(lambda product: product['price'],items))
print(prices)
def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item

items_with_taxes_list = list(map(add_taxes,items))
print(items_with_taxes_list)
items_with_taxes_dict = {item['product']: item['price'] + item['taxes'] for item in items_with_taxes_list}
print(items_with_taxes_dict)