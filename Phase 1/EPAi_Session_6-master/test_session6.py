import pytest
import random
import string
import session6
import os
import inspect
import re
import math

README_CONTENT_CHECK_FOR = [
    'poker',
    'Player A',
    'Player B',
    'lambda',
    'map',
    'zip',
]

deck_of_cards = ['spades-2', 'spades-3', 'spades-4', 'spades-5', 'spades-6', 'spades-7', 'spades-8', 'spades-9', 'spades-10', 
'spades-jack', 'spades-queen', 'spades-king', 'spades-ace', 'clubs-2', 'clubs-3', 'clubs-4', 'clubs-5', 'clubs-6', 'clubs-7', 
'clubs-8', 'clubs-9', 'clubs-10', 'clubs-jack', 'clubs-queen', 'clubs-king', 'clubs-ace', 'hearts-2', 'hearts-3', 'hearts-4', 
'hearts-5', 'hearts-6', 'hearts-7', 'hearts-8', 'hearts-9', 'hearts-10', 'hearts-jack', 'hearts-queen', 'hearts-king', 
'hearts-ace', 'diamonds-2', 'diamonds-3', 'diamonds-4', 'diamonds-5', 'diamonds-6', 'diamonds-7', 'diamonds-8', 'diamonds-9', 
'diamonds-10', 'diamonds-jack', 'diamonds-queen', 'diamonds-king', 'diamonds-ace']

CHECK_FOR_FUNCTIONS = [
    'deck_with_lambda_map_zip',
    'deck_without_lambda_map_zip',
    'poker'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_required_functions():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for w in CHECK_FOR_FUNCTIONS:
        assert w not in functions, 'You have not implemented required functions'







