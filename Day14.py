# Loops in python
""" 
Sometimes a programmer wants to execute a group of statements a certain number of times.
This can be done using loops. Based on this loops are further classified into following types; for loop, while loop, nested loops.

"""
# For loop 
""" 
For loops can iterate over a sequence of iterable objects in python.
Iteriating over a sequence is nothing but iterating over strings, lists,
tuples, sets and dictionaries. 

"""
name = "AlisTamang"
for i in name:
    print(i)
    if (i == 'T'):
        print("Starting the last name")

#iterate over a list

colors = ["Red","Blue", "Green"] 

for color in colors:
    print(color)
    for i in color:
        print(i)
    
# range()
# We use range() function if we want to iterate over a certain number of times.
for k in range(5):
    print(k)

for k in range(1,9): # passing stop argument
    print(k)
    
    
for k in range(1,9,2): # passing step argument
    print(k)