import random
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
As mentioned above, Python docstrings are strings used right after the defination of a function, method, class,
or module (like in Example). They are used to document our code.
we can access these docstring using the doc attribute.
"""
#PEP 8
""" PEP 8 is a document that provides gudlenes and best practises on how to write python code. It was written in 2001 by Guido van Rossum, Barry
warsaw and Nick Coghlan. The primary focus of PEP 8 is to improve readability and consistency of python code.
PEP stands for Python Enhancement Proposal , and there are several of them. A PEP is a document that describes a new 
featurs proposed for python and documents aspects of python, like design and style, for the community."""

def generate_joke():
    """
    This function generates a random joke from a predefined list.

    Returns:
        str: A random joke.
    """
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the chicken go to the seance? To talk to the other side!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]
    return random.choice(jokes)

print(generate_joke())
print(generate_joke.__doc__)
