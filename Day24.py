#DocStrings
#Python docstrings are the string literals that appear right after the defination of a function, method, class or module.

def square(n):
    ''' Takes in a number n, returns the square of n''' #docstring
    print(n**2)
    
square(5)
print(square.__doc__) #printing the docstring


# Python Comments vs Doctstrings
#Python comments
""" 
Comments are descriptions that help prgrammers better understand the intent and functionality of the program.
They are completely ingonred by the python interpreter.
"""
# Python docstrings
""" 
As mentioned above, Python docstrings are string 
"""