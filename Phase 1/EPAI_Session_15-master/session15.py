from collections import namedtuple
from datetime import datetime


def read_csv(file_name):
    '''This function takes a csv file name and creates an iterator for reading the data'''
    data_types = ['INT', 'STRING', 'STRING', 'STRING', 'DATE', 'INT', 'STRING', 'STRING', 'STRING']

    def cast(data_type, value):
        '''This function changes the data format to required format'''
        if data_type == 'DOUBLE':
            return float(value)
        elif data_type == 'DATE':
            if '/' in value:
                return datetime.strptime(value, '%m/%d/%Y')
            else:
                return datetime.strptime(value, '%m-%d-%Y')
        elif data_type == 'INT':
            return int(value)
        else:
            return str(value)

    def cast_row(data_types, data_row):
        '''This function changes the data format of the whole record to required format'''
        return [cast(data_type, value) 
                for data_type, value in zip(data_types, data_row)]
    with open(file_name) as file:
        Car = namedtuple('Car', next(iter(file)).strip('\n').replace(' ','_').split(','))
        for line in iter(file):
            yield Car(*cast_row(data_types,line.strip('\n').split(',')))

cars = read_csv('nyc_parking_tickets_extract-1.csv')

counter_dict = dict()
for car in cars:
    if not(car.Vehicle_Make in counter_dict.keys()):
        counter_dict[car.Vehicle_Make] = 0
    counter_dict[car.Vehicle_Make] += 1

print(counter_dict)
