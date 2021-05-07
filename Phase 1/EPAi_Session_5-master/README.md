# Session 5

#### In this Assignment we have explored function parameters *args and **kwargs and used them to solve time_it function.

#### Inside time_it function we are going to implement five different use cases of functions.



#### time_it:

##### In this time_it function we are going to pass a function for which we are going to calculate average time taken. Also we will use *args for all positional arguments of different functions and **kwargs for all keyword arguments of different functions. Also, we are going to pass one optional keyword argument repetitions with default value 1. Inside time_it we are going to implement five different use cases for five different functions.



#### print:

##### Inside time_it we are going to implement an use case for print function. As print is already defined in python we are not going to define it, we are just going to use it for passed arguments. Here, we can pass as many positional arguments and two string type keyword argument as sep and end.



#### squared_power_list:

##### Inside time_it the second function we are going to implement is squared_power_list function. Here we are going  to pass one positive int or float type number for which we are going to calculate power of an incremental range starting from start value to end value. End value should always be grater than start value.



#### polygon_area:

##### Inside time_it the third function we are going to implement is polygon_area. Here we are going to pass one int or float positional argument i.e. length of side of polygon which is going to be positive and grater than zero and one keyword argument as no of sides of polygon. It can only vary between 2 to 6 as we are not going to implement area for no of sides more than 6. So we will only calculate area for equilateral triangle, square, pentagon and hexagon. We are going to implement area as follows:

1. Area of triangle: 0.433 * a^2
2. Area of square: a^2
3. Area of pentagon: 1.720477 * a^2
4. Area of hexagon: 2.598076 * a^2



#### temp_converter:

##### Inside time_it the forth function we are going to implement is temp_converter. Here we are going to pass one int or float positional argument i.e. temperature and one keyword argument as type of temperature as celsius or fahrenheit. Now if temperature is given is celsius we are going to convert temperature in fahrenheit and visa versa.



#### speed_converter:

##### Inside time_it the fifth function we are going to implement is speed_converter. Here we are going to pass one int or float positional argument i.e. speed which can only be non zero positive number and two keyword argument as distance and time. In distance we can pass four different types as kilometer, meter, foot, yard and in time we can pass five different type as milisecond, second, minute, hour, day. Now, our input should always be kilometer per hour. For conversion we are going to refer the following details:

1. 1 kilometer = 1000 meter
2. 1 kilometer = 3280.84 foot
3. 1 kilometer = 1093.6133333333 yard
4. 1 hour = 60 minutes
5. 1 hour = 3600 seconds
6. 1 hour = 3600000 miliseconds
7. 1 hour = 0.041667 day