#is vs == in python
""" 
In Python, is and  == are both comparison operators that can be used to check if two values are equal. However, there are some important 
 differences between the two that you should be aware of.
 The is operator compares the values of the objects. This means that is will only return True if the objects being compared are exact same 
 object in memory, while == will return True if the objects have same value.
"""

#is vs == in python

a = "Hello"
b = "Hello"

print(a is b)    #exact location of object in memory
print( a == b)   # value

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True, because b is the same object as a
print(a is c)  # False, because c is a different object with the same contents

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True, because the contents of a and b are the same
print(a == c)  # True, because the contents of a and c are the same
