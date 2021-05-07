import pytest
import random
import string
import session8
import os
import inspect
import re
import math

README_CONTENT_CHECK_FOR = [
    'closer',
    'docstring',
    'add',
    'mul',
    'div',
    'global',
    'dictionary',
    'multiple',
    'different dictionaries',
    'fibonacci'
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
    lines = inspect.getsource(session8)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session8, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_docstring_check():
    functions = inspect.getmembers(session8, inspect.isfunction)
    for function in functions:
        assert len(function[1].__doc__) > 0

def test_docstring_check_grater_50():
    def fn_with_dockstring():
        '''Doc String present. All Test Cases passed..........'''
        pass 
    assert session8.dockstring_check()(fn_with_dockstring) == True

def test_docstring_check_less_50():
    def fn_with_dockstring():
        '''Doc String present. All Test Cases passed'''
        pass 
    assert session8.dockstring_check()(fn_with_dockstring) == False

def test_docstring_check_null():
    def fn_with_dockstring():
        ''''''
        pass 
    assert session8.dockstring_check()(fn_with_dockstring) == False

def test_docstring_check_without_docstring():
    def fn_with_dockstring():
        pass
    assert session8.dockstring_check()(fn_with_dockstring) == False

def test_fibonacci_series():
    fn = session8.fibonacci_series()
    assert fn()== 0
    assert fn()== 1
    assert fn()== 1
    assert fn()== 2
    assert fn()== 3
    assert fn()== 5
    assert fn()== 8
    assert fn()== 13
    assert fn()== 21

def test_counter_global_add_div_mul_count_check():
    def add(a, b):
        '''This function returns summation value of the two arguments a & b'''
        return a + b
    def mul(a, b):
        '''This function returns multiplication value of the two arguments a & b'''
        return a*b
    def div(a, b):
        '''This function returns division value of the two arguments a & b'''
        return a/b if b!=0 else 0    
    fn_add = session8.counter_global(add)
    fn_mul = session8.counter_global(mul)
    fn_div = session8.counter_global(div)
    fn_add(0,0)
    fn_add(2,5)
    fn_add(8,0)
    fn_add(3,-5)
    fn_add(-9,-5)
    fn_mul(0,0)
    fn_mul(3,-7)
    fn_mul(-9,0)
    fn_mul(0,4)
    fn_div(0,4)
    fn_div(5,0)
    fn_div(0,0)
    fn_div(2,5)
    fn_div(3,2)
    assert session8.counter_dict['add'] == 5
    assert session8.counter_dict['mul'] == 4
    assert session8.counter_dict['div'] == 5

def test_counter_multiple_user_add_div_mul_count_check():
    user1 = dict()
    user2 = dict()
    def add(a, b):
        '''This function returns summation value of the two arguments a & b'''
        return a + b
    def mul(a, b):
        '''This function returns multiplication value of the two arguments a & b'''
        return a*b
    def div(a, b):
        '''This function returns division value of the two arguments a & b'''
        return a/b if b!=0 else 0
    counter_user1 = session8.counter_multiple_user(user1)
    counter_user2 = session8.counter_multiple_user(user2)
    counter_user1(add,2,3)
    counter_user1(add,3,0)
    counter_user1(add,4,3)
    counter_user1(mul,0,0)
    counter_user1(mul,6,9)
    counter_user1(div,5,0)
    counter_user1(div,2,3)
    counter_user1(div,10,3)
    
    counter_user2(add,3,9)
    counter_user2(add,2,0)
    counter_user2(mul,3,0)
    counter_user2(mul,-9,8)
    counter_user2(mul,3,1)
    counter_user2(mul,0,0)
    counter_user2(div,0,0)
    counter_user2(div,0,3)
    assert counter_user1(div,5,6)[1] == {'add': 3, 'mul': 2, 'div': 4}
    assert counter_user2(div,5,0)[1] == {'add': 2, 'mul': 4, 'div': 3}

