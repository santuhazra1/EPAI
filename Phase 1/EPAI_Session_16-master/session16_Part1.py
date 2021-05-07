from collections import namedtuple
from datetime import datetime


def read_csv(file_name, data_types = False):
    '''This function takes a csv file name and creates an iterator for reading the data'''

    def cast(data_type, value):
        '''This function changes the data format to required format'''
        if data_type == 'DOUBLE':
            return float(value)
        elif data_type == 'DATE':
            value = value[:10]
            if '/' in value:
                return datetime.strptime(value, '%Y/%m/%d')
            else:
                return datetime.strptime(value, '%Y-%m-%d')
        elif data_type == 'INT':
            return int(value)
        else:
            return str(value)

    def cast_row(data_types, data_row):
        '''This function changes the data format of the whole record to required format'''
        if data_types == False:
            return [cast("STRING", value) 
                    for value in data_row]
        else:
            return [cast(data_type, value) 
                    for data_type, value in zip(data_types, data_row)]

    with open(file_name) as file:
        Data = namedtuple('Data', next(iter(file)).strip('\n').replace(' ','_').split(','))
        for line in iter(file):
            yield Data(*cast_row(data_types,line.strip('\n').split(',')))


class Merge:
    def __init__(self, file_name_list, data_type_list):
        self.file_name_list = file_name_list
        self.data_type_list = data_type_list

    def __iter__(self):
        # return IteratorMerge.iterator_gen(self.iterator)
        return self.IteratorMerge(self)

    @staticmethod
    def iterator_gen(itr_list):
        fields = next(itr_list[0])._fields
        for i in range(1, len(itr_list)):
            fields = fields + next(itr_list[i])._fields[1:]
        DataN = namedtuple("DataN", fields)
        for line1, line2, line3, line4 in zip(*itr_list):
            yield DataN(*line1, *line2[1:], *line3[1:], *line4[1:])

    class IteratorMerge:
        def __init__(self, iterator_obj):
            self.iterator_obj = iterator_obj
 
        def __iter__(self):
            return self
            
        def __next__(self):
            employment = read_csv(self.iterator_obj.file_name_list[0], self.iterator_obj.data_type_list[0])
            personal_info = read_csv(self.iterator_obj.file_name_list[1], self.iterator_obj.data_type_list[1])
            update_status = read_csv(self.iterator_obj.file_name_list[2], self.iterator_obj.data_type_list[2])
            vehicles = read_csv(self.iterator_obj.file_name_list[3], self.iterator_obj.data_type_list[3])

            return Merge.iterator_gen([employment, personal_info, update_status, vehicles])


data_types_empl = ['STRING', 'STRING', 'STRING', 'STRING']

data_types_pinfo = ['STRING', 'STRING', 'STRING', 'STRING', 'STRING']

data_types_ustatus = ['STRING', 'DATE', 'DATE']

data_types_vcl = ['STRING', 'STRING', 'STRING', 'INT']

file_name = ['employment.csv', 'personal_info.csv', 'update_status.csv', 'vehicles.csv']

data_type = [data_types_empl, data_types_pinfo, data_types_ustatus, data_types_vcl]

all_data = Merge(file_name, data_type)


for x in next(iter(all_data)):
    print(x)


data_filter = filter(lambda x: x.last_updated < datetime.strptime('3/1/2017', '%d/%m/%Y'),next(iter(all_data)))

for x in data_filter:
    print(x)

counter_dict_male = dict()
counter_dict_female = dict()
for data in next(iter(all_data)):
    if data.gender == "Female":
        if not(data.vehicle_make + data.gender in counter_dict_female.keys()):
            counter_dict_female[data.vehicle_make + data.gender] = 0
        counter_dict_female[data.vehicle_make + data.gender] += 1
    else:
        if not(data.vehicle_make + data.gender in counter_dict_male.keys()):
            counter_dict_male[data.vehicle_make + data.gender] = 0
        counter_dict_male[data.vehicle_make + data.gender] += 1

male_key = [data_dict_key[:-4] for data_dict_key,data_dict_value  in counter_dict_male.items() if data_dict_value == max(counter_dict_male.values())]
print(male_key)

female_key = [data_dict_key[:-6] for data_dict_key,data_dict_value  in counter_dict_female.items() if data_dict_value == max(counter_dict_female.values())]
print(female_key)

