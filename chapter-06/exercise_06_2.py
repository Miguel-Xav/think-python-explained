import math


def hypot(a, b):
    return math.sqrt(a**2 + b**2) #Do the classic equation of the Pythagoras
# The return will attribute the value of square root of the sum to the function

value = round(hypot(1, 2), 2) #I`ve used the round to make the value have only two decimal places
print(value) # Print the value

'''
The hypot  is a "Fruitful" function
An Fruitful function is a function that store a value inside of her

One example of a void function (non fruitful) is the print
The print function not have a value attached, it`s for a "final action"

Remember:   Fruitful Function: Transform data
            Void Function: It`s Terminal (execute tasks)
'''