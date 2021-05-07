import math

__all__ = ["tanh"]
__derivative__ = ["dtanh"]

def tanh(theta, angle = "radians"):
    '''This function returns tanh of value passed'''
    if not (type(theta) == int or type(theta) == float):
        raise ValueError('Non-Integer value error..')
    else:
        output = math.tanh(math.radians(theta)) if angle=="degrees" else math.tanh(theta)
    print(f"Value of tanh({theta}) is {output}")
    return output

def dtanh(theta, angle = "radians"):
    '''This function returns derivative of tanh of value passed'''
    if not (type(theta) == int or type(theta) == float):
        raise ValueError('Non-Integer value error..')
    else:
        output = (1 / (math.cosh(math.radians(theta)) ** 2)) if angle=="degrees" else (1 / (math.cosh(theta) ** 2))
    print(f"Value of derivative of tanh({theta}) is {output}")
    return output

