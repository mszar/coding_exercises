# list methods

# exercise 1 
# remove fruits from basket2 that are present in basket1

basket1 = ['banana', 'kiwifruits', 'grapefruits', 'apples', 'apricots', 'nectarines', 'oranges', 'peaches', 'pears', 'lemons']
basket2 = ['apples', 'grapes', 'apricots', 'dragonfruits', 'peaches', 'pears', 'limes', 'papaya']

for fruit in basket1:
    if fruit in basket2:
        basket2.remove(fruit)

print("Basket 1: " + str(basket1))
print("Basket 2: " + str(basket2))

# transfer fruits from basket1 to basket2 until the amount in basket2 becomes more or equal to amount in basket1

while len(basket1) > len(basket2):
        item_to_transfer = basket1.pop()
        basket2.append(item_to_transfer)
print("Basket1 after transfer:" + str(basket1) + " items: " + str(len(basket1)))
print("Basket2 after transfer:" + str(basket2) + " items: " + str(len(basket2)))


# exercise 2

# equation for circular paraboloid: create a dictionary that stores the mapping from 
# the pair of coordinates (x,y) to the z coordinate

circ_parab = dict()

range_x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
range_y = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]

for x in range_x:
    for y in range_y:
        z = ((x**2/1) + (y**2/1))
        key = (x,y)
        circ_parab[key] = z

print(circ_parab)    
