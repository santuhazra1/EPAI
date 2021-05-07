import math

__all__ = ["log"]
__derivative__ = ["dlog"]

def log(value, base = "e"):
    '''This function returns logarithm of value passed'''
    if not (type(value) == int or type(value) == float):
        raise ValueError('Non-Integer value error..')
    else:
        output = math.log(value) if base=="e" else math.log(value, base)
    print(f"Value of log({value}) with base {base} is {output}")
    return output

def dlog(value, base = "e"):
    '''This function returns derivative of logarithm of value passed'''
    if not (type(value) == int or type(value) == float):
        raise ValueError('Non-Integer value error..')
    else:
        output = (1 / value) if base=="e" else (1 / (math.log(base) * value))
    print(f"Value of derivative of log({value}) with base {base} is {output}")
    return output
