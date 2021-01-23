# all below exercises are prepared by datacamp team

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


# exercise 5

# regular expressions - define a pattern to search for valid temperature

import re

text = "Let's consider the following temperatures using the Celsius scale: +23 C, 0 C, -20.0 C, -2.2 C, -5.65 C, 0.0001 C. To convert them to the Fahrenheit scale you have to multiply the number by 9/5 and add 32 to the result. Therefore, the corresponding temperatures in the Fahrenheit scale will be: +73.4 F, 32 F, -4.0 F, +28.04 F, 21.83 F, +32.00018 F."
pattern = re.compile(r'[+-]?\d+\.?\d* [CF]')
print(re.findall(pattern, text))

# create object storing matches using finditer then loop over item properties

matches_storage = re.finditer(pattern, text)

for match in matches_storage:
    print('Matching sequence: ' + match.group())
    print('Start index: ' + str(match.start()))
    print('End index: ' + str(match.end()))


# exercise 6 

# prepare regular expression that splits string and prepare 
# string with name of the movie and director

movies = ['1984, 1984, Michael Radford',
 'The Good, the Bad and the Ugly, 1966, Sergio Leone',
 'Terminator 2: Judgment Day, 1991, James Cameron',
 "Harry Potter and the Philosopher's Stone, 2001, Chris Columbus",
 'Back to the Future, 1985, Robert Zemeckis',
 'No Country for Old Men, 2007, Joel Coen, Ethan Coen']

pattern = re.compile(r', \d+, ')

movies_without_year = []

for movie in movies:
    split_result = re.split(pattern, movie)
    movie_and_director = ', '.join(split_result)
    movies_without_year.append(movie_and_director)
    
for movie in movies_without_year:
    print(movie)