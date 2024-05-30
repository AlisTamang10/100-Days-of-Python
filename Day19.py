#Introduction to lists
""" 
- Lists are ordered collection of data items
- They store multiple items in a single variable.
- Lists are seperate by commas and enclosed with in square brackets[]
- Lists are changeable, meaning we can alter them after creation.
"""

Lists = [2,3,5,7,8,'a',True]
Color = ["Green ","Red","Blue","Violet"]
print(type(Lists))
# retriving the data from lists
#List index
print(Lists[2])
print(Color[0]) #positive indexing

#Negative Indexing
print(Color[-2])
print(Lists[len(Lists)-3]) #positve index

#Check wether an item exist in the list

if "Red" in Color:
    print("It exists")
else:
    print("No")
#Same thing applies for string as well  
if "li" in "Alis":
    print("Exist")
    
# Range of INdex
""" 
You can print a range of lists items by specifing where you want to start , where do you want to end and 
if you want to skip the elements in between the range
"""
animals = ["cat", 'dog','bat','pig','horse','goat']
print(animals[2:-2]) #using neagtive index
print(animals[1:3]) #using positive index
print(animals[0:-1:2]) #using jump Index

#List Comprehension 
""" 
List comprehensions are used for creating new lists from other iterables like list, tuples, dictionaries,
sets and even in arrays and strings.
Syntax : List = [Expression(item) for item in iterable if condn]
"""
lst = [i  for i in range(5)]
print(lst)
lst = [(i * "*" ) for i in range(10) if i%2 == 0]
print(lst)
