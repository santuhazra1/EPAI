import math

__all__ = ["tan"]
__derivative__ = ["dtan"]

def tan(theta, angle = "radians"):
    '''This function returns tan of value passed'''
    if not (type(theta) == int or type(theta) == float):
        raise ValueError('Non-Integer value error..')
    else:
        output = math.tan(math.radians(theta)) if angle=="degrees" else math.tan(theta)
    print(f"Value of tan({theta}) is {output}")
    return output

def dtan(theta, angle = "radians"):
    '''This function returns derivative of tan of value passed'''
    if not (type(theta) == int or type(theta) == float):
        raise ValueError('Non-Integer value error..')
    else:
        output = (1 / (math.cos(math.radians(theta)) ** 2)) if angle=="degrees" else (1 / (math.cos(theta) ** 2))
    print(f"Value of derivative of tan({theta}) is {output}")
    return output
