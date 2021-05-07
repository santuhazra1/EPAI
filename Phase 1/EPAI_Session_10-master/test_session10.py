import pytest
import random
import string
import session10
import os
import inspect
import re
import math

README_CONTENT_CHECK_FOR = [
    'namedtuple',
    'profiles',
    'blood',
    'age',
    'location',
    'dictionaries',
    'random',
    'fake',
    'company',
    'stock',
    'market'
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
    lines = inspect.getsource(session10)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session10, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_docstring_check():
    functions = inspect.getmembers(session10, inspect.isfunction)
    for function in functions:
        assert len(function[1].__doc__) > 0

def test_function_namedtuple_profile_check():
    bloodgroup,mean_loc,max_age,avg_age = session10.namedtuple_profile(10)
    bGroupFlag = False
    for bldgrp in ['A+', 'O-', 'O+', 'AB+', 'B+', 'AB-', 'B-', 'A-']:
        if bldgrp == bloodgroup:
            bGroupFlag = True
            pass
    assert bGroupFlag == True, "Bloodgroup must be one of the listed group"
    assert len(mean_loc) != 0
    assert max_age > 0
    assert avg_age > 0

def test_function_dict_profile_check():
    bloodgroup,mean_loc,max_age,avg_age = session10.dict_profile(10)
    bGroupFlag = False
    for bldgrp in ['A+', 'O-', 'O+', 'AB+', 'B+', 'AB-', 'B-', 'A-']:
        if bldgrp == bloodgroup:
            bGroupFlag = True
            pass
    assert bGroupFlag == True, "Bloodgroup must be one of the listed group"
    assert len(mean_loc) != 0
    assert max_age > 0
    assert avg_age > 0

def test_function_stock_market_chek():
    stock_details = session10.stock_market(100)
    assert stock_details.open > 0
    assert (stock_details.high > stock_details.open) & (stock_details.high > stock_details.close)
    assert stock_details.close > 0