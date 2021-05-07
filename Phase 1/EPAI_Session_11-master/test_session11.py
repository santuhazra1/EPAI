import pytest
import random
import string
import os
import inspect
import re
import math
import glob
import jpg_to_png, png_to_jpg, img_resizer, img_cropper

README_CONTENT_CHECK_FOR = ['PIL','jpeg','png','jpg','resize','crop','module',
'p2j','j2p','res_p','res_w','res_h','crp_px','crp_p']

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

def test_indentations_jpg_to_png():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(jpg_to_png)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_indentations_png_to_jpg():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(png_to_jpg)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_indentations_img_resizer():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(img_resizer)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_indentations_img_cropper():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(img_cropper)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(jpg_to_png, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
    functions = inspect.getmembers(png_to_jpg, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
    functions = inspect.getmembers(img_resizer, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
    functions = inspect.getmembers(img_cropper, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_docstring_check():
    functions = inspect.getmembers(jpg_to_png, inspect.isfunction)
    for function in functions:
        assert len(function[1].__doc__) > 0
    functions = inspect.getmembers(png_to_jpg, inspect.isfunction)
    for function in functions:
        assert len(function[1].__doc__) > 0
    functions = inspect.getmembers(img_resizer, inspect.isfunction)
    for function in functions:
        assert len(function[1].__doc__) > 0
    functions = inspect.getmembers(img_cropper, inspect.isfunction)
    for function in functions:
        assert len(function[1].__doc__) > 0

def test_function_jpg_to_png():
    path = ".\\images\\"
    jpg_to_png.convert(path)
    files_grabbed = glob.glob(path + '*.*')
    for file in files_grabbed:
        assert "jpg" not in file

def test_function_png_to_jpg():
    path = ".\\images\\"
    png_to_jpg.convert(path)
    files_grabbed = glob.glob(path + '*.*')
    for file in files_grabbed:
        assert "png" not in file


