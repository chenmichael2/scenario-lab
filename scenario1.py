# NEO: filter: splitting one chaotic list into smaller, more organized lists
# MICHAEL: map: performing a mathematic operation on a list to acquire a new set of values 
# '''
num = [20, 11, 7]
def math_op(n):
    return n + 8

result = map(math_op, num)
print(list(result))

# '''
# Filling out a cafe menu from an array of data and categorizing it by types of food/drink?
# MICHAEL : And Filter to display specific data by a type you need so filter(food) and getting back Pancakes, Burgers and not getting drinks bacK?
# '''

foods = [
    {
        "category": 'breakfast',
        "name": "pancakes", 
    },
    {
        "category": "breakfast", 
        "name": "bacon"
    },
    {
        "category": "lunch",
        "name": "sandwich"
    }, 
    {
        "category": "dinner",
        "name": "steak"
    }, 
    {
        "category": "lunch",
        "name": "chicken bake"
    },
    {
        "category": "lunch", 
        "name": "burger"
    }
]

lunches = filter(lambda food: food.get('category') == 'lunch', foods)
lunch = list(lunches)
# print(lunch)
food = map(lambda x: x.get('name'), lunch)
print('lunch foods', list(food))



# '''
# NEO : map - determine the total for items in a store after taxes/discounts
# MICHAEL:filter - get a list of items that are listed at a high discount right now
# '''
discount = [
    {
        "name": "wallet",
        "price": 15,
        "discount": 15
    },
    {
        "name": "stuffed bear",
        "price": 34.99,
        "discount": 30
    },
    {
        "name": "national treasure",
        "price": 10000000,
        "discount": 95
    },
    {
        "name": "Rome's laptop",
        "price": 300,
        "discount": 100 
    },
    {
        "name": "Sick shoes",
        "price": 1598,
        "discount": 70
    },
    {
        "name": "Chicken Nuggets",
        "price": 9,
        "discount": 10 
    },
]

def discounted_item_list(arr):
    parse = filter(lambda i: i.get('discount') >= 50, arr)
    # print('parse', list(parse))
    fifty_plus = list(parse)
    # print('fifty plus', fifty_plus)
    cheap_items = map(lambda x: x.get('name'), fifty_plus)
    print('name', list(cheap_items))

discounted_item_list(discount)

# '''
# MICHAEL: inflation on products increase to 7% for map, 
def inflation_increase(item_arr):
    inflation = map(lambda i: i.get('price') * 1.07, item_arr)
    # print('discounted', list(inflation))
    return list(inflation)

cart = inflation_increase(discount)
print('reciept', cart)

# NEO: filter is to take out the things i want in a list
# '''


# '''
# MICHAEL: use map to get a total value in a cart
def total(c):
    num = 0
    for i in range(len(c)):
        num += c[i]
        # print(c[i])
    return num

print('total before discounts', total(cart))


# NEO: use filter to sort a list by any value
# '''

