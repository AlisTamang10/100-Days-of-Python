#Tuples
""" 
Tuples are ordered collection of data items. They store multiple items in a single variable.
Tuple items are seperated by commas and enclosed with round brackets(). Tuples are unchangebale meaning we can not alter them
after creation
"""
var = (1,5,6,'a','b','c')
foods = ('rice','soup','bread','peas')
print(type(var))
print(var[3])
print(foods[2])

# Check for item: we can check if a given item is present in the tuple. Thos os done using the in keyword.
if "soup" in foods:
    print("Soup is present in the tuple.")
else:
    print("Not present in the tuple.")
    
#Range of index
""" 
You can print a range of tuple items by specifying where do you want to start, where do you want to end and 
if you want to skip elements.
"""
print(foods[-3:-1]) #neagtive indexing
print(var[3:5])    #positive indexing


#Manipulating Tuples
#Tuples are immutable, hence if you want to make changes on tuples , first you must convert tuple to a list.
 
countires = ("Nepal","India","China","Bangladesh","Bhutan")
temp = list(countires)
temp.append("Srilanka")
temp.pop(2)
countires = tuple(temp)
print(countires)  #output - ('Nepal', 'India', 'Bangladesh', 'Bhutan', 'Srilanka')

#but to concatinate two tuples we don't have to convert into list
mix = var + foods
print(mix)

#Some methods of count
print(mix.count(5))

# index()
res = mix.index('soup')
print(res)

#len () method
print(len(mix))