# Raise Custom Error
""" 
In python we can raise custom error by using raise key word
"""
a = int(input("Enter the value between 5 and 9: "))

if(a < 5 or a > 9):
    raise ValueError("Value should be between 5 and 9")

# Define Custom Exceptions
#In python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

# Example of using custom Exception
 
class MycustomException(Exception):
    pass

def riskyFunction(n):
    if n < 0:
        raise MycustomException("Number is negative")
    
    return n ** 2

try:
    result = riskyFunction(-5)
    
except MycustomException as e:
    print("Caught Exception as ", e)
    
else:
    print(result)
    