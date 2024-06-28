# lambda function
""" 
In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword
Lambda functions are often used in situations where a small function is required for a short peroid of time. They are 
commenly used as arguments to higher-order functions, such as map, filter, and reduce.
"""
#lambda function

#simple function 
def doublee(x):
    return x * 2
print(doublee(5))

#now using lambda function
double = lambda x: x *2
cube = lambda x: x*x*x
avg = lambda x, y : (x+y)/2

def apply(fx, value):
    return 6 + fx(value)

print(double(5))
print(cube(5))
print(avg(2,3))
print(apply(cube,5))