
__all__ = ["relu"]
__derivative__ = ["drelu"]

def relu(value):
    '''This function returns relu of value passed'''
    if not (type(value) == int or type(value) == float):
        raise ValueError('Non-Integer value error..')
    else:
        output = value if value > 0 else 0
    print(f"Value of relu({value}) is {output}")
    return output

def drelu(value):
    '''This function returns derivative of relu of value passed'''
    if not (type(value) == int or type(value) == float):
        raise ValueError('Non-Integer value error..')
    else:
        output = 1 if value > 0 else 0
    print(f"Value of derivative of relu({value}) is {output}")
    return output