import pytest
import random
import string
import session5
import os
import inspect
import re
import math

README_CONTENT_CHECK_FOR = [
    'time_it',
    'print',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter',
    'polygon',
    'triangle',
    'square',
    'pentagon',
    'hexagon',
    'power',
    'celsius',
    'fahrenheit',
    'kilometer',
    'meter',
    'foot',
    'yard',
    'milisecond',
    'second',
    'hour',
    'minute',
    'day',
    '*args',
    '**kwargs',
    'repetitions'
]

CHECK_FOR_FUNCTIONS = [
    'time_it',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

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
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"
       
def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_required_functions():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for w in CHECK_FOR_FUNCTIONS:
        assert w not in functions, 'You have not implemented required functions'

# repetitions value tests
def test_non_integer_repetitions_value():
    with pytest.raises(ValueError):
        session5.time_it(print,1,2,3, sep='-', end= ' ***\n', repetitions='jh')

def test_zero_or_negative_repetitions_value():
    with pytest.raises(ValueError):
        session5.time_it(print,1,2,3, sep='-', end= ' ***\n', repetitions=0)
    with pytest.raises(ValueError):
        session5.time_it(print,1,2,3, sep='-', end= ' ***\n', repetitions=-2)

def test_invalid_repetitions_provides_relevant_message():
    with pytest.raises(ValueError, match=r"Invalid .*"):
        session5.time_it(print,1,2,3, sep='-', end= ' ***\n', repetitions=0)
    with pytest.raises(ValueError, match=r"Invalid .*"):
        session5.time_it(print,1,2,3, sep='-', end= ' ***\n', repetitions='jh')

# print function tests
def test_invalid_keyword_argument_valueerror_for_print():
    with pytest.raises(ValueError):
        session5.time_it(print,1,2,3,4,5,6, sep='-', end= ' ***\n', myparam = "awsm", repetitions=5)

def test_invalid_keyword_name_valueerror_for_print():
    with pytest.raises(ValueError):
        session5.time_it(print,1,2,3,4,5,6, sepsap='-', ended= ' ***\n', repetitions=5)

def test_print_function_check():
    assert session5.time_it(print,1,2,3, sep='-', end= ' ***\n', repetitions=1000)[0] > 0.0
    assert session5.time_it(print,1, sep='-', end= ' ***\n', repetitions=1000)[0] > 0.0
    assert session5.time_it(print,1,2,3,4,5,6, sep='$', end= ' #\n', repetitions=1000)[0] > 0.0

# squared_power_list function tests
def test_null_positional_argument_squared_power():
    with pytest.raises(ValueError):
        session5.time_it(session5.squared_power_list, start=0, end=5, repetitions=1000)

def test_multiple_positional_argument_squared_power():
    with pytest.raises(ValueError):
        session5.time_it(session5.squared_power_list,2,3, start=0, end=5, repetitions=1000)

def test_non_int_or_float_positional_argument_squared_power():
    with pytest.raises(ValueError):
        session5.time_it(session5.squared_power_list,'f', start=0, end=5, repetitions=1000)   

def test_negative_int_positional_argument_squared_power():
    with pytest.raises(ValueError):
        session5.time_it(session5.squared_power_list,-6, start=0, end=5, repetitions=1000) 

def test_null_start_or_end_argument_squared_power():
    with pytest.raises(ValueError):
        session5.time_it(session5.squared_power_list,2, start=0, repetitions=1000)   
              
def test_more_than_2_keyword_argument_squared_power():
    with pytest.raises(ValueError):
        session5.time_it(session5.squared_power_list,2, start=0,end=7, x=5, repetitions=1000) 

def test_invalid_keyword_argument_name_squared_power():
    with pytest.raises(ValueError):
        session5.time_it(session5.squared_power_list,2, starting=0,endless=7, repetitions=1000)  

def test_non_integer_start_or_end_argument_squared_power():
    with pytest.raises(ValueError):
        session5.time_it(session5.squared_power_list,2, start='k',end='l', repetitions=1000)  

def test_non_integer_start_or_end_argument_squared_power():
    with pytest.raises(ValueError):
        session5.time_it(session5.squared_power_list,2, start='k',end='l', repetitions=1000) 

def test_start_grater_than_end_argument_squared_power():
    with pytest.raises(ValueError):
        session5.time_it(session5.squared_power_list,2, start=5,end=2, repetitions=1000) 

def test_squared_power_function_check():
    assert session5.time_it(session5.squared_power_list,2, start=2,end=6, repetitions=1000) [0] > 0.0
    assert session5.time_it(session5.squared_power_list,2, start=2,end=6, repetitions=1000) [1] == [4, 8, 16, 32, 64]
    assert session5.time_it(session5.squared_power_list,3.5, start=3,end=7, repetitions=1000) [0] > 0.0
    assert session5.time_it(session5.squared_power_list,3.5, start=3,end=7, repetitions=1000) [1] == [42.875, 150.0625, 525.21875, 1838.265625, 6433.9296875]

# polygon_area function tests
def test_null_side_length_polygon_area():
    with pytest.raises(ValueError):
        session5.time_it(session5.polygon_area, sides = 3, repetitions=1000)

def test_multiple_side_length_polygon_area():
    with pytest.raises(ValueError):
        session5.time_it(session5.polygon_area,2, 3, sides = 3, repetitions=1000)

def test_noint_or_float_side_length_polygon_area():
    with pytest.raises(ValueError):
        session5.time_it(session5.polygon_area,'ok', sides = 3, repetitions=1000)

def test_zero_or_negative_side_length_polygon_area():
    with pytest.raises(ValueError):
        session5.time_it(session5.polygon_area,0, sides = 3, repetitions=1000)
    with pytest.raises(ValueError):
        session5.time_it(session5.polygon_area,-4, sides = 3, repetitions=1000)

def test_null_no_of_sides_polygon_area():
    with pytest.raises(ValueError):
        session5.time_it(session5.polygon_area, 15, repetitions=1000)

def test_multiple_keyword_argument_polygon_area():
    with pytest.raises(ValueError):
        session5.time_it(session5.polygon_area, 15, sides = 3, myvar= 8, repetitions=1000)

def test_no_of_sides_name_polygon_area():
    with pytest.raises(ValueError):
        session5.time_it(session5.polygon_area, 15, myside = 3, repetitions=1000)

def test_non_int_or_float_no_of_sides_polygon_area():
    with pytest.raises(ValueError):
        session5.time_it(session5.polygon_area, 15, myside = 'ok', repetitions=1000)

def test_invalid_no_of_sides_polygon_area():
    with pytest.raises(ValueError):
        session5.time_it(session5.polygon_area, 15, myside = 7, repetitions=1000)
    with pytest.raises(ValueError):
        session5.time_it(session5.polygon_area, 15, myside = 1, repetitions=1000)

def test_polygon_area_function_check():
    assert session5.time_it(session5.polygon_area, 15, sides = 3, repetitions=1000) [0] > 0.0
    assert session5.time_it(session5.polygon_area, 15, sides = 4, repetitions=1000) [0] > 0.0 
    assert session5.time_it(session5.polygon_area, 15, sides = 5, repetitions=1000) [0] > 0.0
    assert session5.time_it(session5.polygon_area, 15, sides = 6, repetitions=1000) [0] > 0.0
    assert math.isclose(session5.time_it(session5.polygon_area, 15, sides = 3, repetitions=1000) [1], 97.43,rel_tol = 0.01)
    assert math.isclose(session5.time_it(session5.polygon_area, 15, sides = 4, repetitions=1000) [1], 225.0,rel_tol = 0.01)
    assert math.isclose(session5.time_it(session5.polygon_area, 15, sides = 5, repetitions=1000) [1], 387.11,rel_tol = 0.01)
    assert math.isclose(session5.time_it(session5.polygon_area, 15, sides = 6, repetitions=1000) [1], 584.57,rel_tol = 0.01)

# temp_converter function tests
def test_null_temp_value_temp_converter():
    with pytest.raises(ValueError):
        session5.time_it(session5.temp_converter, temp_given_in = 'c', repetitions=1000)

def test_multiple_temp_value_temp_converter():
    with pytest.raises(ValueError):
        session5.time_it(session5.temp_converter, 100,200, temp_given_in = 'c', repetitions=1000)

def test_non_int_or_float_temp_value_temp_converter():
    with pytest.raises(ValueError):
        session5.time_it(session5.temp_converter, 'no', temp_given_in = 'c', repetitions=1000)

def test_null_temp_format_temp_converter():
    with pytest.raises(ValueError):
        session5.time_it(session5.temp_converter, 100, repetitions=1000)

def test_multiple_key_argument_temp_converter():
    with pytest.raises(ValueError):
        session5.time_it(session5.temp_converter, 100, var = 8, temp_given_in = 'c', repetitions=1000)

def test_temp_format_name_temp_converter():
    with pytest.raises(ValueError):
        session5.time_it(session5.temp_converter, 100, temp_given_out = 'c', repetitions=1000)

def test_non_str_type_temp_format_temp_converter():
    with pytest.raises(ValueError):
        session5.time_it(session5.temp_converter, 100, temp_given_in = 6, repetitions=1000)

def test_invalid_type_temp_format_temp_converter():
    with pytest.raises(ValueError):
        session5.time_it(session5.temp_converter, 100, temp_given_in = 'x', repetitions=1000)

def test_polygon_area_function_check():
    assert session5.time_it(session5.temp_converter, 100, temp_given_in = 'c', repetitions=1000) [0] > 0.0
    assert session5.time_it(session5.temp_converter, 90.5, temp_given_in = 'f', repetitions=1000) [0] > 0.0 
    assert math.isclose(session5.time_it(session5.temp_converter, 100, temp_given_in = 'c', repetitions=1000) [1], 212.0,rel_tol = 0.01)
    assert math.isclose(session5.time_it(session5.temp_converter, 90.5, temp_given_in = 'f', repetitions=1000) [1], 32.5,rel_tol = 0.01)

# speed_converter function tests
def test_null_speed_value_speed_converter():
    with pytest.raises(ValueError):
        session5.time_it(session5.speed_converter, dist='km', time='day', repetitions=1000)

def test_multiple_speed_value_speed_converter():
    with pytest.raises(ValueError):
        session5.time_it(session5.speed_converter, 100, 200, dist='km', time='day', repetitions=1000)

def test_non_int_or_float_speed_value_speed_converter():
    with pytest.raises(ValueError):
        session5.time_it(session5.speed_converter, 'yes', dist='km', time='day', repetitions=1000)

def test_zero_or_negative_or_float_speed_value_speed_converter():
    with pytest.raises(ValueError):
        session5.time_it(session5.speed_converter, 0, dist='km', time='day', repetitions=1000)
    with pytest.raises(ValueError):
        session5.time_it(session5.speed_converter, -4, dist='km', time='day', repetitions=1000)

def test_null_dist_time_value_speed_converter():
    with pytest.raises(ValueError):
        session5.time_it(session5.speed_converter, 100, repetitions=1000)

def test_multiple_keyword_argument_speed_converter():
    with pytest.raises(ValueError):
        session5.time_it(session5.speed_converter, 100, dist='km', time='day', day = 'good', repetitions=1000)

def test_dist_time_name_speed_converter():
    with pytest.raises(ValueError):
        session5.time_it(session5.speed_converter, 100, d='km', t='day', repetitions=1000)

def test_non_str_dist_time_speed_converter():
    with pytest.raises(ValueError):
        session5.time_it(session5.speed_converter, 100, dist=5, time=4, repetitions=1000)

def test_invalid_dist_time_value_speed_converter():
    with pytest.raises(ValueError):
        session5.time_it(session5.speed_converter, 100, dist='x', time='y', repetitions=1000)

def test_polygon_area_function_check():
    assert session5.time_it(session5.speed_converter, 100, dist='km', time='day', repetitions=1000) [0] > 0.0
    assert session5.time_it(session5.speed_converter, 45.6, dist='ft', time='m', repetitions=1000) [0] > 0.0 
    assert math.isclose(session5.time_it(session5.speed_converter, 100, dist='km', time='day', repetitions=1000) [1], 2400.0, rel_tol = 0.01)
    assert math.isclose(session5.time_it(session5.speed_converter, 45.6, dist='ft', time='m', repetitions=1000) [1], 2493.4383,rel_tol = 0.01)


