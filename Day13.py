#Match case statement
"""
To implement switch-case like characteristics very similar to if else functionality, we use a match case in python.
If you are coming from a C, C+++ or Java like laguage , you must have heard of switch case
statement. 
A match statement will compare a given variable's value to different shapes, also refered to as the pattern.
The main idea is to keep on comparing the vairable with all present patterns until it fits into one.
"""
x = int(input("Enter the number: "))

match x :
    
    case 0:
        print("Value of x is Zero")
    
    case 4 if x % 2 == 0 : #case with if condition 
        print("Value of X is 4")
        
    case _ if x < 10:        # empty case with if statement
        print("Value of x is less than 10")
        
    case _:                   # Default Case 
        print("Default Case",x)
        
        
    