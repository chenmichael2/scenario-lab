# '''
# NEO: filter: splitting one chaotic list into smaller, more organized lists
# MICHAEL: map: performing a mathematic operation on a list to acquire a new set of values 
# '''

# '''
# Filling out a cafe menu from an array of data and categorizing it by types of food/drink?
# NEO : Like map to make the arrays organized for display on a page?
# So like.... Cola, Sprite, Coffee?
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

#hoping this works

# '''
# NEO : map - determine the total for items in a store after taxes/discounts

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

