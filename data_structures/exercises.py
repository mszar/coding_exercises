#all below exercises are prepared by datacamp team

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


# exercise 3

# create caesar cipher - encryption requires two arguments: 
# text to encrypt and integer key denoting the shift

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(text, key):
    encrypted_text = ''
    for char in text.lower():
        idx = (alphabet.index(char) + key) % len(alphabet)
        encrypted_text = encrypted_text + alphabet[idx]
    return encrypted_text

print(encrypt('datacamp',10))

def decrypt(text, key):
    encrypted_text = ''
    for char in text.lower():
        idx = alphabet.index(char) - key
        encrypted_text = encrypted_text + alphabet[idx]
    return encrypted_text


# exercise 4 

# create word list from the given string

text = 'StRing ObJeCts haVe mANy inTEResting pROPerTies'

word_list = text.split(' ')
print(word_list)

# every oher word uppercase and lowercase

for i in range(len(word_list)):
    if i % 2 == 0:
        word_list[i] = word_list[i].upper()
    else:
        word_list[i] = word_list[i].lower()
print(word_list)

# join the words from new string list

new_text = ' '.join(word_list)
print(new_text)