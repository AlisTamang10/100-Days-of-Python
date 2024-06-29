# Map , Filter and Reduce
""" 
In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements 
and return a new sequence. These functions are known as higher-order functions, as the take other functions as arguments .

Map
The map function applies a function to each element in a sequence and returns a new sequence containing the transforemd elements. 

Filter
The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new 
sequence containing only the elements that meet the predicate. 

Reduce
The reduce function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools moudle
in Python.
"""
#map
def cube(x):
    return x*x*x

list_num = [1,2,3,4,5,6]
newlist = list(map(cube,list_num))
print(newlist)                      #output - [1, 8, 27, 64, 125, 216]

#filter
def filter_function(a):
    return a >= 4

filtered_list = list(filter(filter_function, list_num))
print(filtered_list)                # output - [4, 5, 6]

#reduce
from functools import reduce

numbers = [3,23,431,21,34]

def mysum(x,y):
    return x +y 

sum = reduce(mysum, numbers)    # output - 512
sum2 = reduce(mysum, list_num)  # output - 21
print(sum, sum2)  