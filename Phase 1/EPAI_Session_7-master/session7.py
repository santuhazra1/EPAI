import math
from functools import reduce
import random

# Problem 1:
def fibonacci(n):
    '''This function takes an input n and creates a list of n no of fibonacci series'''
    fibonacci_series = []
    for i in range(1,n+1):
        # First Fibonacci number is 0 
        if i==1: 
            fibonacci_series.append(0)
        # Second Fibonacci number is 1 
        elif i==2:  
            fibonacci_series.append(1)
        else:
            fibonacci_series.append(fibonacci_series[i-2] + fibonacci_series[i-3])
    return fibonacci_series

def fibonacci_check(n):
    '''This function checks for a given number n if its fibonacci or not and returns an 
    output i.e. fibonacci or not a fibonacci no'''
    return "fibonacci" if bool(list(filter(lambda x: x==n,fibonacci(10000)))) else "not a fibonacci no"

# Problem 2.1:
def even_odd_summation(l1, l2):
    '''This function takes two lists as input and adds even no for the first list 
    and odd number the second list and returns summation result as a list'''
    return [x + y for x, y in zip(l1, l2) if x % 2 == 0 and y % 2 != 0]

# Problem 2.2:
def vowel_stripping(string):
    '''This function takes a string as an input strips out vowels and returns stripted out string'''
    return "".join([x for x in string if x not in('a','e','i','o','u')])

# Problem 2.3:
def relu(l1):
    '''This function takes a list as an input and acts as Relu i.e. when an element is -ve it returns 0 else the element'''
    return [0 if x < 0 else x for x in l1]

# Problem 2.4:
def sigmoid(l1):
    '''This function takes a list as an input and acts as sigmoid function and returns a list of sigmoid output'''
    return [(1 / (1 + math.exp(-x))) for x in l1]

# Problem 2.5:
def char_shift(string):
    '''This function takes a string as an input and shifts each character by 5 and returns shifted string'''
    return "".join([chr(ord(x)+5) if (ord(x)+5) <= 122 else chr(96 + (ord(x)+5) - 122) for x in string])

# Problem 3:
file1 = open("swear_words.txt","r")
swear_words = [x.rstrip() for x in file1.readlines()]

def swear_word_check(swear_para):
    '''This function takes and input of a paragraph and check if swear word 
    is present in the paragraph and returns a list of swear words that is present'''
    return [x for x in swear_words if x in swear_para.lower()]

# Problem 4.1:
def even_add_reduce(l1):
    '''This function takes an input as a list and gives output as a summation of even no in the list using reduce'''
    even_add = lambda x, y: x + y if (x % 2 == 0) and (y % 2 == 0) else (bool(x % 2 == 0) * x) + (bool(y % 2 == 0) * y)
    return reduce(even_add, l1)

# Problem 4.2:
def biggest_char(string):
    '''This function takes an input as a string and returns the biggest output character in the string'''
    biggest_chr = lambda x, y: x if ord(x) > ord(y) else y
    return reduce(biggest_chr, string)

# Problem 4.3: 
def no_add_3rd(l1):
    '''This function takes a list as an input and returns summation of every 3ed element'''
    return reduce(lambda x, y: x + y, l1[::3])

# Problem 5: 
def random_numberplate_generator():
    '''This function generates a list 15 random number plate'''
    return ["KA" + str(random.randint(10,99)) + random.choice([chr(x) for x in range(65,91)]) +\
        random.choice([chr(x) for x in range(65,91)]) + str(random.randint(1000,9999)) for x in range(15)]

# Problem 6:
def plate(state, range_start, range_end):
    '''This function takes a string for state e.g. KA, WB and start and end range of last 4 digit'''
    return [state + str(random.randint(10,99)) + random.choice([chr(x) for x in range(65,91)]) +\
        random.choice([chr(x) for x in range(65,91)]) + str(random.randint(range_start,range_end)) for x in range(15)]

def plate_partial(state):
    '''This partial function takes the above function and we can only pass state information as start 
    and end range of last 4 digit is already hardcoded'''
    return plate(state, range_start = 5000,range_end = 5010)
