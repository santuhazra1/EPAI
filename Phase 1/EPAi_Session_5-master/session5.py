import time
import math

def squared_power_list(x, start, end):
    if x <= 0:
        raise ValueError('Negative or zero positional argument. Please provide one positive argument for powered list')

    elif start > end:
        raise ValueError('Invalid start and end argument. Please provide start value less than end value')

    else:
        powered_list =[]
        for i in range(start, end + 1):
            value = x ** i
            powered_list.append(value)
    return powered_list

def polygon_area(side_length, sides):
    if sides <= 2 or sides >=7:
        raise ValueError('Invalid no of sides. Please provide no of sides between 3 to 6')
    elif side_length <= 0:
        raise ValueError('Invalid side length. Side length must be grater than zero')
    else:
        if sides == 3:
            area = (math.sqrt(3)/4) * (side_length**2)
        elif sides == 4:
            area = side_length ** 2
        elif sides == 5:
            area = 0.25 * math.sqrt(5 * (5 + (2 * math.sqrt(5)))) * (side_length ** 2)
        elif sides == 6:
            area = 1.5 * math.sqrt(3) * (side_length**2)
    return area

def temp_converter(temp, temp_given_in):
    if temp_given_in == "f" or temp_given_in == "F":
        temp_converted = (temp - 32) * (5/9)
    elif temp_given_in == "c" or temp_given_in == "C":
        temp_converted = (temp * (9/5)) + 32
    else:
        raise ValueError('Invalid Temperature given in format value.')
    return temp_converted

def speed_converter(speed, dist, time):
    if speed <= 0:
        raise ValueError('speed cannopt be Negative or zero. Please provide one positive argument for speed')
    elif not(dist == "km" or dist == "m" or dist == "ft" or dist == "yrd") and  not(time == "ms" or time == "s" or time == "m" or time == "hr" or time == "day"):
        raise ValueError('Invalid distance and time value for conversion. Distance and time should be either of km/m/ft/yrd and ms/s/m/hr/day consecutively')
    else:
        if dist == "km":
            speed_converted = speed
        elif dist == "m":
            speed_converted = speed * 1000
        elif dist == "ft":
            speed_converted = speed * 3280.84
        elif dist == "yrd":
            speed_converted = speed * 1093.61

        if time == "ms":
            speed_converted = speed_converted / 3600000
        if time == "s":
            speed_converted = speed_converted / 3600
        if time == "m":
            speed_converted = speed_converted / 60            
        if time == "day":
            speed_converted = speed_converted * 24
    return speed_converted


def time_it(fn, *args, repetitions= 1, **kwargs):
    start = time.time()
    output = []
    if type(repetitions) != int:
        raise ValueError('Invalid repetitions number. Repetitions number must be an integer.')
    elif repetitions <= 0:
        raise ValueError('Invalid repetitions number. Repetitions number must be grater than 0.')
    else:
        for i in range(0,repetitions):
            if fn.__name__ == "print":
                if len(kwargs) > 2:
                    raise ValueError('More than two keyword argument. Please provide only sep and end value')
                elif len(kwargs) == 2 and not(("sep" in kwargs) and ("end" in kwargs)):
                    raise ValueError('Invalid keyword argument name. Please provide sep and end value')
                else:
                    var = args
                    if len(kwargs) == 0:
                        kwargs = {
                                    'sep': " ",
                                    'end': "\n"
                                    }
                    while len(var) > 2:
                        x , y, *var = var
                        fn(x,y,sep = kwargs['sep'], end = "")
                        fn(kwargs['sep'],sep = "", end = "")
                    if not bool(var):
                        fn(var,sep = kwargs['sep'], end = kwargs['end'])
                    elif len(var) ==1:
                        fn(var[0],sep = kwargs['sep'], end = kwargs['end'])                        
                    elif len(var) ==2:
                        fn(var[0],var[1],sep = kwargs['sep'], end = kwargs['end'])

            elif fn.__name__ == "squared_power_list":
                if not bool(len(args)):
                    raise ValueError('Null positional argument. Please provide one argument for powered list')
                elif len(args) > 1:
                    raise ValueError('Multiple positional argument. Please provide only one argument for powered list')
                elif type(args[0]) != int and type(args[0]) != float:
                    raise ValueError('Positional argument is not integer or float type. Can not return a powered list other than type integer or float')

                elif not bool(len(kwargs)):
                    raise ValueError('Null keyword argument. Please provide start and end value')
                elif len(kwargs) > 2:
                    raise ValueError('More than two keyword argument. Please provide only start and end value')
                elif not(("start" in kwargs) and ("end" in kwargs)):
                    raise ValueError('Invalid keyword argument name. Please provide start and end value')
                elif type(kwargs["start"]) != int or type(kwargs["end"]) != int:
                    raise ValueError('Invalid keyword argument. Please provide integer start and end value')
                else:
                    output = fn(args[0], start = kwargs["start"], end = kwargs["end"]) 

            elif fn.__name__ == "polygon_area":
                if not bool(len(args)):
                    raise ValueError('Null positional argument. Please provide one argument for side length')
                elif len(args) > 1:
                    raise ValueError('Multiple positional argument. Please provide only one argument for side length')
                elif type(args[0]) != int and type(args[0]) != float:
                    raise ValueError('Positional argument is not integer or float type. Can not return a area for non integer or float side length') 

                elif not bool(len(kwargs)):
                    raise ValueError('Null keyword argument. Please provide no of sides for area calculation')
                elif len(kwargs) > 1:
                    raise ValueError('More than two keyword argument. Please provide only one sides value')
                elif not(("sides" in kwargs)):
                    raise ValueError('Invalid keyword argument name. Please provide sides value')
                elif type(kwargs["sides"]) != int:
                    raise ValueError('Invalid keyword argument. Sides can only be integer')     
                else:
                    output = fn(args[0], sides = kwargs["sides"])           

            elif fn.__name__ == "temp_converter":
                if not bool(len(args)):
                    raise ValueError('Null positional argument. Please provide one argument for temperature')
                elif len(args) > 1:
                    raise ValueError('Multiple positional argument. Please provide only one argument for temperature')
                elif type(args[0]) != int and type(args[0]) != float:
                    raise ValueError('Positional argument is not integer or float type. Can not return a converted temperature for non integer or float value') 

                elif not bool(len(kwargs)):
                    raise ValueError('Null keyword argument. Please provide temp given in value')
                elif len(kwargs) > 1:
                    raise ValueError('More than two keyword argument. Please provide only one Temperature given in value')
                elif not(("temp_given_in" in kwargs)):
                    raise ValueError('Invalid keyword argument name. Please provide Temperature given in value')
                elif type(kwargs["temp_given_in"]) != str:
                    raise ValueError('Invalid keyword argument. Temperature given in can only be string')
                else:
                    output = fn(args[0], temp_given_in = kwargs["temp_given_in"]) 

            elif fn.__name__ == "speed_converter":
                if not bool(len(args)):
                    raise ValueError('Null positional argument. Please provide one argument for speed conversion')
                elif len(args) > 1:
                    raise ValueError('Multiple positional argument. Please provide only one argument for speed conversion')
                elif type(args[0]) != int and type(args[0]) != float:
                    raise ValueError('Positional argument is not integer or float type. Can not convert speed of a value other than type integer or float') 

                elif not bool(len(kwargs)):
                    raise ValueError('Null keyword argument. Please provide dist and time value')
                elif len(kwargs) > 2:
                    raise ValueError('More than two keyword argument. Please provide only dist and time value')
                elif not(("dist" in kwargs) and ("time" in kwargs)):
                    raise ValueError('Invalid keyword argument name. Please provide dist and time value')
                elif type(kwargs["dist"]) != str or type(kwargs["time"]) != str:
                    raise ValueError('Invalid keyword argument. Please provide string type dist and time value')
                else:
                    output = fn(args[0], dist = kwargs["dist"], time = kwargs["time"])                                 

    end = time.time()   
    return (end - start)/repetitions, output