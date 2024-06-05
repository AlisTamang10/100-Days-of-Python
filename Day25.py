# Recursion
""" 
Recursion is the process of defining something in terms of itself.

A physical world example would be to place two parallel mirror facing each other. Any object in 
between them would be reflected recursively.

Python Recursive function
In Python, we know that a function can call other functions. It is even possible for the function to call itself.
These types of construct are termed as recursive functions.

"""

def factorial(n):
    if (n == 0 or n==1):
        return 1
    else:
        return n * factorial(n-1) # calling the same function 
    
print(factorial(3))
print(factorial(4))

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        fib = fibonacci(n-1) + fibonacci(n-2)
        return fib
    
print(fibonacci(4))
