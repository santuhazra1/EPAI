import math

__all__ = ["sin"]
__derivative__ = ["dsin"]

def sin(theta, angle = "radians"):
    '''This function returns sin of value passed'''
    if not (type(theta) == int or type(theta) == float):
        raise ValueError('Non-Integer value error..')
    else:
        output = math.sin(math.radians(theta)) if angle=="degrees" else math.sin(theta)
    print(f"Value of sin({theta}) is {output}")
    return output

def dsin(theta, angle = "radians"):
    '''This function returns derivative of sin of value passed'''
    if not (type(theta) == int or type(theta) == float):
        raise ValueError('Non-Integer value error..')
    else:
        output = math.cos(math.radians(theta)) if angle=="degrees" else math.cos(theta)
    print(f"Value of derivative of sin({theta}) is {output}")
    return output

