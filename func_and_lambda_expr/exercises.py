# all below exercises are prepared by datacamp team

# exercise 1
# Define the function sort_types, it takes variable number of 
# arguments and check if each argument is number or a string

def sort_types(*args):
    nums, strings = [], []
    for arg in args:
        if isinstance(arg, (int,float)):
            nums.append(arg)
        elif isinstance(arg, str):
            strings.append(arg)
    return (nums, strings)

print(sort_types('abc',1,'dse',2,3,4,'asd'))

# exercise 2
# Define the function key_types, it takes arbitraty number of 
# keyword arguments. It should return new dictionary: the keys 
# are unique object types and the associated values represent lists

def key_types(**kwargs):
    dict_type = dict()
    for key, value in kwargs.items():
        if type(value) in dict_type:
            dict_type[type(value)].append(key)
        else:
            dict_type[type(value)] = [key]
    return dict_type

chck = key_types(a=1, b=2, c=(1, 2), d=3.1, e=4.2)

# exercise 3
# Define the function sort_all_types. It takes positional and keyword
# arguments. Find all numbers and strings in both arguments.

def sort_all_types(*args, **kwargs):
    nums1, strings1 = sort_types(*args)
    nums2, strings2 = sort_types(*kwargs.values())
    return (nums1 + nums2, strings1 + strings2)
  
chck = sort_all_types(1, 2.0, 'dog', 5.1, num1 = 0.0, num2 = 5, str1 = 'cat')


# exercise 4
# Prepare lambda expresion 

# Take x and return x squared if x > 0 and 0, otherwise
squared_no_negatives = lambda x: x**2 if x > 0 else 0

# Take a list of integers nums and leave only even numbers
get_even = lambda nums: [n for n in nums if n % 2 == 0]

# Take strings s1, s2 and list their common characters
common_chars = lambda s1, s2: set(x for x in s1 
                                    for y in s2 if x == y)
print(common_chars('pasta', 'pizza'))


# exercise 5
# convert functions to lambda expressions

def func1(x, y):
    if x >= y:
        return x
    return y

lambda1 = lambda x,y: x if x >= y else y

def func2(s):
    d = dict()
    for c in set(s):
        d[c] = s.count(c)
    return d

lambda2 = lambda s: dict([[i,s.count(i)] for i in set(s)])

import math
def func3(*nums):
    squared_nums = [n**2 for n in nums]
    sum_squared_nums = sum(squared_nums)

    return math.sqrt(sum_squared_nums)

lambda3 = lambda *nums: math.sqrt(sum([n**2 for n in nums]))

print(str(lambda3(3, 4)))


# exercise 6
# sort words by length using lambda expression

words = ['car', 'bag', 'job', 'time', 'cell', 'call', 'area', 'item', 'unit', 'truck', 'phone', 'shape', 'plane', 'leader', 'height', 'tequila', 'chicken', 'country', 'service', 'creature', 'interview', 'advantage', 'government', 'atmosphere', 'transaction']
words.sort(key=lambda s: len(s))

# sort words by the last character in a string

words.sort(key= lambda s: s[-1])

# sort words by the total amount of certain characters

words.sort(key=lambda s: s.count('a') + s.count('b') + s.count('c'))


# exercise 7
# use map function to find the minimal length 

def my_zip(*args):
    lengths = list(map(len, args))
    min_length = min(lengths)
    tuple_list = []
    for i in range (0,min_length):
        mapping = map(lambda s: s[i], args)
        tuple_list.append(tuple(mapping))
    return tuple_list

result = my_zip([1, 2, 3], ['a', 'b', 'c', 'd'], 'DataCamp')
print(list(result))


# exercise 8 
# Using filter exclude all the numbers from nums divisible by 3 or 5

nums = [*range(0,100)]
fnums = filter(lambda i: i % 3 != 0 and i % 5 != 0, nums)

# Return the string without its vowels
string = 'Ordinary Least Squares'
vowels = ['a','e','i','o','u']
fstring = filter(lambda s: s.lower() not in vowels, string)
print(''.join(fstring))

# Filter all the spells in spells with more than two 'a's
spells = ['riddikulus',
 'obliviate',
 'sectumsempra',
 'avada kedavra',
 'alohomora',
 'lumos',
 'expelliarmus',
 'expecto patronum']

fspells = filter(lambda x: x.count('a') > 2, spells)
print(list(fspells))


# exercise 9 
# Reverse a string using reduce()

from functools import reduce 

string = 'DataCamp'
inv_string = reduce(lambda x, y: y+x ,string)
print('Inverted string = ' + inv_string)

# Find common items shared among all the sets in sets
sets = [{1, 4, 8, 9}, {2, 4, 6, 9, 10, 8}, {9, 0, 1, 2, 4}]
common_items = reduce(lambda x, y: x.intersection(y), sets)
print('common items = ' + str(common_items))

# Convert a number sequence into a single number
nums = [5, 6, 0, 1]
num = reduce(lambda x, y: 10*x + y, nums)
print(str(nums) + ' is converted to ' + str(num))

# exercise 10
# Calculate an average value of the sequence of numbers

# Calculate an average value of the sequence of numbers
def average(nums):
    if len(nums) == 1:  
        return nums[0]
    n = len(nums)
    return (nums[0] + (n - 1) * average(nums[1:])) / n  

print(average([1, 2, 3, 4, 5]))


# exercise 11
# Write an expression to get the k-th element of the series 

get_elmnt = lambda k: ((-1)**k)/(2*k+1)

# Write an expression to get the k-th element of the series 
get_elmnt = lambda k: ((-1)**k)/(2*k+1)

def calc_pi(n):
    curr_elmnt = get_elmnt(n)
    if n == 0:
    	return 4
    return 4 * curr_elmnt + calc_pi(n-1)

print("approx = {}, theor = {}".format(calc_pi(500), math.pi))

