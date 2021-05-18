# module1

print(f'________________ Running {__name__} ______________')

def pprint_dict(header, d):
    print('\n\n ____________________________________________ ')
    print(f'***** {header} ******')
    for key, value in d.items():
        print(key, value)
    print('_____________________________________________\n\n')

# let's use this function to print glopals dict

pprint_dict('module1.globals', globals())

print(f'__________________ End of {__name__} __________________')