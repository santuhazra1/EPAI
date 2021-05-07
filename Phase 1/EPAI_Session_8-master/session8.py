# Question: 1

def dockstring_check():
    '''We have to initialize this function once and it will return a function which 
    checks length of docstring of a function and returns boolean value..'''
    length = 50
    def docstr_test(fn):
        '''This function checks the length of the doc string of the 
        function passed to it and returns true or false value..'''
        return bool(fn.__doc__) and (len(fn.__doc__) > length)
    return docstr_test


# Question: 2

def fibonacci_series():
    '''We have to initialize this function once and it will return a function 
    which outputs next fibonacci no each time we run it..'''
    first_no = 0
    nxt_no = 1
    count = 0
    def next_fibonacci():
        '''This function returns next fibonacci no each time we run it..'''
        nonlocal first_no, nxt_no, count
        if count == 0:
            fibonacci_no = first_no
        elif count == 1:
            fibonacci_no = nxt_no
        else:
            fibonacci_no = first_no + nxt_no
            first_no = nxt_no
            nxt_no = fibonacci_no
        count += 1
        return fibonacci_no
    return next_fibonacci


# Question: 3

counter_dict = dict()

def counter_global(fn):
    '''We have to initialize this function once and it will return a function 
    which counts how many times a function was called from the above was called'''
    global counter_dict
    counter_dict[fn.__name__] = 0
    def inner(*args, **kwargs):
        '''This function returns add/div/mul as passed and prints the counts of them'''
        counter_dict[fn.__name__] += 1
        print('{0} has been called {1} times'.format(fn.__name__, counter_dict[fn.__name__]))
        return fn(*args, **kwargs)
    return inner

# Question: 4

def counter_multiple_user(counter):
    '''We have to initialize this function once and it will return a function 
    which counts how many times a function was called for multiple user from the above was called'''
    counter = {'add': 0, 'mul': 0, 'div': 0}
    def inner(*args, **kwargs):
        '''This function returns add/div/mul as passed and prints the counts of them'''
        nonlocal counter
        counter[args[0].__name__] += 1
        print('{0} has been called {1} times'.format(args[0].__name__, counter[args[0].__name__]))
        return args[0](args[1], args[2]), counter
    return inner
