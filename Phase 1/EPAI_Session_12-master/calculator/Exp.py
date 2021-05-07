import math

__all__ = ["e"]
__derivative__ = ["de"]

def e(value):
    '''This function returns exponentional of value passed'''
    if not (type(value) == int or type(value) == float):
        raise ValueError('Non-Integer value error..')
    else:
        output = math.exp(value)
    print(f"Value of e({value}) is {output}")
    return output

def de(value):
    '''This function returns derivative of exponentional of value passed'''
    if not (type(value) == int or type(value) == float):
        raise ValueError('Non-Integer value error..')
    else:
        output = math.exp(value)
    print(f"Value of derivative of e({value}) is {output}")
    return output
