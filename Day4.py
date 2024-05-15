#Data Types and Virables

'''
variable : it is like container that holds data. While creating variables it creates placeholder in memory and assigns some values.
data types : Data type specifies the types of data that variable holds. This is required in programming language 
to do operations without causing any error. 

'''

b = 'Alis'   #String
c = True     #Boolean
d = None     # None Type
# Numeric data
a = 1111123  #Integer
e = 3.144    #float
f = complex(3 + 9)  #complex

# Sequence Data
lis = [1,2,3, 'a','b']   #list type (mutable)
tup = ('apple', 'banana') #tuple (immutable)

# Mapped Data
dict1 = {
    'Name': "Alis",
    'Age' : 21
}

print('Type of c is ', type(c))
print('Type of d is', type(d))
print(f)
print('Type of f is', type(f))
print('Type of lis', type(lis) )
print('Type of tup', type(tup) )
print('Type of dict1', type(dict1) )