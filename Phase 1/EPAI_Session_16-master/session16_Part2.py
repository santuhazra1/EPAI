from collections import namedtuple
from datetime import datetime
import csv
from contextlib import contextmanager
from itertools import islice

# Goal 1
class DataIterator:
    def __init__(self, fname, data_delimiter):
        self._fname = fname
        self.data_delimiter = data_delimiter
        self._f = None

    @staticmethod
    def iterator_gen(file_name, data_delimiter):
        data = csv.reader(file_name, delimiter=data_delimiter, quotechar='"')
        Data = namedtuple('Data', next(data))
        for x in data:
            yield Data(*x)

    def __iter__(self):
        return DataIterator.iterator_gen(self._f, self.data_delimiter)
     
    def __enter__(self):
        self._f = open(self._fname)
        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        if not self._f.closed:
            self._f.close()
        return False

with DataIterator('cars.csv',";") as f:
    for car in islice(f,5):
        print(car)

with DataIterator('personal_info.csv',",") as f:
    for p_info in islice(f,5):
        print(p_info)

# Goal 2

@contextmanager
def open_file(fname, mode='r'):
    f = open(fname, mode)
    try:
        yield f
    finally:
        f.close()

def read_csv(filename,data_delimiter):
    with open_file(filename) as f:
        Data = namedtuple('Data', next(iter(f)).strip('\n').replace(' ','_').split(data_delimiter))
        for row in iter(f):
            yield Data(*row.strip('\n').split(data_delimiter))

cars = read_csv('cars.csv',';')

for car in islice(cars,5):
    print(car)


p_info = read_csv('personal_info.csv',',')

for car in islice(p_info,5):
    print(car)