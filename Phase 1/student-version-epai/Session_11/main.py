# main.py

print(f'________________ Running {__name__} ______________')


import module1

print(module1)

module1.pprint_dict('main.globals', globals())

import sys

print(sys.path)

print("Importing Module1 again")

import module1

del globals()['module1']

# globals()['module1'] = sys.modules['module1']
import module1
module1.pprint_dict('main.globals', globals())


