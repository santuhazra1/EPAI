import pytest
import os
import inspect
import math

README_CONTENT_CHECK_FOR = ['package','sin', 'cos', 'tan', 'tanh', 'relu', 'sigmoid', 'softmax', 'log', 
'e', 'calculator','derivatives']

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

def test_function_docstring_check():
    import calculator
    from calculator import derivative as derivative
    functions = inspect.getmembers(calculator, inspect.isfunction)
    for function in functions:
        assert len(function[1].__doc__) > 0
    functions = inspect.getmembers(derivative, inspect.isfunction)
    for function in functions:
        assert len(function[1].__doc__) > 0

def test_all_function_check():
    import calculator
    assert calculator.sin(math.pi / 2) == 1
    assert calculator.cos(math.pi) == -1
    assert calculator.tan(0) == 0
    assert calculator.tanh(0) == 0
    assert calculator.softmax([1 , 2]) == [0.2689414213699951, 0.7310585786300049]
    assert calculator.e(0) == 1
    assert calculator.log(10,base=10) == 1
    assert calculator.relu(10) == 10
    assert calculator.relu(-10) == 0
    assert calculator.sigmoid(0) == 0.5

def test_all_derivative_function_check():
    from calculator import derivative as derivatives
    assert derivatives.dsin(math.pi) == -1
    assert derivatives.dcos(math.pi / 2) == -1
    assert derivatives.dtan(0) == 1
    assert derivatives.dtanh(0) == 1
    assert derivatives.de(0) == 1
    assert derivatives.dlog(10) == 0.1
    assert derivatives.drelu(10) == 1
    assert derivatives.drelu(-10) == 0
    assert derivatives.dsigmoid(0) == 0.25
    assert derivatives.dsigmoid(1) == 0.19661193324148185


