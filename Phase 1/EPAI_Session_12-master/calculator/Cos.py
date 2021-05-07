import math

__all__ = ["cos"]
__derivative__ = ["dcos"]

def cos(theta, angle = "radians"):
    '''This function returns cos of value passed'''
    if not (type(theta) == int or type(theta) == float):
        raise ValueError('Non-Integer value error..')
    else:
        output = math.cos(math.radians(theta)) if angle=="degrees" else math.cos(theta)
    print(f"Value of cos({theta}) is {output}")
    return output

def dcos(theta, angle = "radians"):
    '''This function returns derivative of cos of value passed'''
    if not (type(theta) == int or type(theta) == float):
        raise ValueError('Non-Integer value error..')
    else:
        output = -math.sin(math.radians(theta)) if angle=="degrees" else -math.sin(theta)
    print(f"Value of derivative of cos({theta}) is {output}")
    return output
