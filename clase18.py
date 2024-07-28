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
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19
    return new_item

items_with_taxes_list = list(map(add_taxes,items))
print(items)
print(items_with_taxes_list)