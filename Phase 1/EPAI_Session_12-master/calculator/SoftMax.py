import math

__all__ = ["softmax"]

def softmax(list_a):
    '''This function returns softmax value of list passed'''
    if not type(list_a) == list:
        raise ValueError('Non-list value error..')
    elif len(list_a) < 2:
        raise ValueError('Cannot evaluate softmax of a single value..')
    else:
        total_sum = sum([math.exp(x) for x in list_a])
        output = [math.exp(x)/total_sum for x in list_a]
    print(f"SoftMax of ({list_a}) is {output}")
    return output

print(softmax([1 , 2]))