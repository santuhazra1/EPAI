import math

__all__ = ["sigmoid"]
__derivative__ = ["dsigmoid"]

def sigmoid(value):
    '''This function returns sigmoid of value passed'''
    if not (type(value) == int or type(value) == float):
        raise ValueError('Non-Integer value error..')
    else:
        output = 1 / (1 + math.exp(-value))
    print(f"Value of sigmoid({value}) is {output}")
    return output

def dsigmoid(value):
    '''This function returns derivative of sigmoid of value passed'''
    if not (type(value) == int or type(value) == float):
        raise ValueError('Non-Integer value error..')
    else:
        output = sigmoid(value) * (1 - sigmoid(value))
    print(f"Value of derivative of sigmoid({value}) is {output}")
    return output
