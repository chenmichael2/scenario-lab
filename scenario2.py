# '''
# NEO: filter: splitting one chaotic list into smaller, more organized lists
list1 = [1, 22, 45, 2, 36, 81, 79, 12, 8]

result = filter(lambda x: x < 25, list1)
print(list(result))

result2 = filter(lambda x: x >= 25, list1)
print(list(result2))
# MICHAEL: map: performing a mathematic operation on a list to acquire a new set of values 
# '''

# '''
# Filling out a cafe menu from an array of data and categorizing it by types of food/drink?
# NEO : Like map to make the arrays organized for display on a page?
# So like.... Cola, Sprite, Coffee?
cafe_menu = [{
            'name': 'Pancakes',
            'type': 'food' 
            }, 
            {
            'name': 'Burgers',
            'type': 'food'
            }, 
            {
            'name': 'Steak',
            'type': 'food'
            }, 
            {
            'name': 'Cola',
            'type': 'drink'
            }, 
            {
            'name': 'Sprite',
            'type': 'drink'
            },
            {
            'name': 'Coffee',
            'type': 'drink'
            }]

lunches = filter(lambda food: food.get('type') == 'food', cafe_menu)
lunch = list(lunches)
food = map(lambda x: x.get('name'), lunch)
print('food', list(food))


# MICHAEL : And Filter to display specific data by a type you need so filter(food) and getting back Pancakes, Burgers and not getting drinks bacK?
# '''

# '''
# NEO : map - determine the total for items in a store after taxes/discounts
store_items = [
    {
        'name': 'milk',
        'cost': 2.84
    },
    {
        'name': 'bread',
        'cost': 2.44
    },
    {
        'name': 'cereal',
        'cost': 3.28
    },
    {
        'name': 'chips',
        'cost': 4.12
    }]

# item_cost = map(lambda x: x.get('cost'), store_items)
# print(list(item_cost))
# number = 0
total = 0
for i in range(len(list(store_items))):
    item_cost = map(lambda x: x.get('cost'), store_items)
    
    total += list(item_cost)[i]

print(round(total * 1.06, 2))

# MICHAEL:filter - get a list of items that are listed at a high discount right now
# '''



# '''
# MICHAEL: inflation on products increase to 7% for map, 

# NEO: filter is to take out the things i want in a list
# '''


# '''
# MICHAEL: use map to get a total value in a cart
# NEO: use filter to sort a list by any value
# '''
