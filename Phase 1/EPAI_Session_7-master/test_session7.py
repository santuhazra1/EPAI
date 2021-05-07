import pytest
import random
import string
import session7
import os
import inspect
import re
import math

README_CONTENT_CHECK_FOR = [
'fibonacci',
'even',
'odd',
'vowel',
'strips',
'relu',
'sigmoid',
'shifts',
'swear',
'reduce',
'biggest',
'character',
'numberplate',
'partial'
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
    lines = inspect.getsource(session7)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_even_odd_summation_function_check():
    assert session7.even_odd_summation([1,2,3,4],[4,5,6,7])== [7, 11]
    assert session7.even_odd_summation([10,11,12,13],[21,22,23,24]) == [31, 35]

def test_fibonacci_function_check():
    assert session7.fibonacci_check(2) == "fibonacci"
    assert session7.fibonacci_check(4) == "not a fibonacci no"
    assert session7.fibonacci_check(5) == "fibonacci"
    assert session7.fibonacci_check(20) == "not a fibonacci no"

def test_vowel_stripping_function_check():
    assert session7.vowel_stripping('python')== 'pythn'
    assert session7.vowel_stripping('deeplearning') == 'dplrnng'

def test_relu_function_check():
    assert session7.relu([1,2,-3,4,-8,2])== [1,2,0,4,0,2]
    assert session7.relu([-21,9,4,-5,3,1]) == [0,9,4,0,3,1]

def test_sigmoid_function_check():
    assert session7.sigmoid([1,2,-3,4,-8,2])== [0.7310585786300049, 0.8807970779778823, 0.04742587317756678, 0.9820137900379085, 0.0003353501304664781, 0.8807970779778823]
    assert session7.sigmoid([-21,9,4,-5,3,1]) == [7.582560422162385e-10, 0.9998766054240137, 0.9820137900379085, 0.0066928509242848554, 0.9525741268224334, 0.7310585786300049]

def test_char_shift_function_check():
    assert session7.char_shift('tsai')== 'yxfn'
    assert session7.char_shift('python') == 'udymts'

file2 = open("swear_para.txt","r")
swear_para = file2.read()

def test_swear_word_check_function_check():
    assert session7.swear_word_check(swear_para)== ['damn', 'fuck', 'shit']

def test_even_add_reduce_function_check():
    assert session7.even_add_reduce([1, 2, 3 , 4, 8])== 14
    assert session7.even_add_reduce([2, 6, 9, 4])== 12

def test_biggest_char_function_check():
    assert session7.biggest_char('python')[0]== 'y'
    assert session7.biggest_char('Machine')[0]== 'n'

def test_no_add_3rd_function_check():
    assert session7.no_add_3rd([1, 2, 5, 6, 8, 9, 2])== 9
    assert session7.no_add_3rd([12, 23, 25, 65, 12, 3, 2])== 79

def test_random_numberplate_generator_function_check():
    assert len(session7.random_numberplate_generator()) == 15
    assert session7.random_numberplate_generator()[0][0:2] =='KA'

def test_plate_partial_function_check():
    assert len(session7.plate_partial('DA')) == 15
    assert session7.plate_partial('DA')[0][0:2] =='DA'
