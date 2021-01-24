# all below exercises are prepared by datacamp team


# exercise 1 

# define the function that create a dictionary from a string where
# each key # represents a unique # character and the value is list 
# containg the indices of this letter

def retrieve_character_indices(string):
    character_indices = dict()
    for index, character in enumerate(string):
        if character in character_indices:
           character_indices[character].append(index)
        if character not in character_indices:
            character_indices[character] = [index]
    return character_indices

print(retrieve_character_indices('eaeaeaebbbb'))


# exercise 2

# list comprehesion - convert the text to lower case and create a word list

import re
spam = 'Dear User,\n\nOur Administration Team needs to inform you that you are reaching the storage limit of your Mailbox account.\nYou have to verify your account within the next 24 hours.\nOtherwise, it will not be possible to use the service.\nPlease, click on the link below to verify your account and continue using our service.\n\nYour Administration Team.'

def create_word_list(string):
    pattern = re.compile(r'\w+')
    words = re.findall(pattern, string)
    return words

words = [word.lower() for word in create_word_list(spam)]

# create a set that will store only unique words

word_set = {word for word in create_word_list(spam)}

# create a dictionary that counts a word apperance in the word list

tuples = [(word, words.count(word)) for word in words]
word_counter = dict(tuples)

# print words that appear in word_counter more than once

for (key,value) in word_counter.items():
    if value > 1:
        print("{}: {}".format(key, value))


# exercise 3

# prime number checker - firstly prepare function which check 
# if a number is prime 

from math import sqrt
cands = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
primes = [num for num in cands if is_prime(num) is True]
print(primes)


# exercise 4

# greatest common divisor - firstly define function which check 
# for greatest common divisior

list1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
list2 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]

def gcd(a,b):
    while b != 0:
        temp_a = a
        a = b
        b = temp_a % b
    return a

coprimes = [(i, j) for i in list1 
                   for j in list2 if gcd(i, j) == 1]


# exercise 5

# combine iterable objects - create a new iterable object, where 
# each element represents a tuple. Each tuple contains list, len 
# of this list and longest word within this list

wlist = [['Python', 'creativity', 'universe'], ['interview', 'study', 'job', 'university', 'lecture'], ['task', 'objective', 'aim', 'subject', 'programming', 'test', 'research']]

def get_longest_word(words):
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

# Create a list of the lengths of each list in wlist

lengths = [len(lists) for lists in wlist]

# Create a list of the longest words in each list in wlist

words = [get_longest_word(word) for word in wlist]

# Combine the resulting data into one iterable object

for item in zip(wlist, lengths, words):
    print(item)


# exercise 6

# Create a list of tuples with lengths and longest words

result = [
    (len(item), get_longest_word(item)) for item in wlist
]

lengths, words = zip(*result)

for item in zip(wlist, lengths, words):
    print(item)


# exercise 7

# Create a dataframe from the wlist variable
# Create a list with tuples of the form (word itself, len of word)

word_lenghts = [ (item, len(item)) for items in wlist for item in items]

print(word_lenghts)
