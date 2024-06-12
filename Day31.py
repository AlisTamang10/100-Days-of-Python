# Exception Handling
""" 
Exception handing is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these
events to avoid the program or system crashing, and without this process,
exceptions would disrupt the normal operation of a program.
"""
#Exceptions in python
""" 
Python has many buit-in exceptions that are raised when your program encounter an error( Something in the program goes wrong)
When these exceptions occur, the python interpreter stops the current process and passes it to the calling process until it is handled. if not handled, the program will crash.
"""

#Python try except
""" 
try..... except blocks are used in python to handle errors and exceptions. The code in try block runs when 
there is no error. If the try block catches the error, then the except block is executed.
"""


try:
    a = int(input("Enter the number: "))
    print(f"Multiplication Table of {a}")
    
    for i in range(1,11):
        print(f"{a} X {i} = {i*a}")
        
except:
    print("Invalid Input")
    
print("End of program")

#Value Error / Index Error

try:
    num =int(input("Enter an integer: "))
    b = [9,8]
    print(b[num])
except ValueError:
    print("Number is not an integer")
    
except IndexError:
    print("Index Error")
    