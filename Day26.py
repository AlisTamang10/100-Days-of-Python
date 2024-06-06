# Sets
""" Sets are unorderd collection of data items. They store multiple items in a single variable.
Set items are seperated by commas and enclosed with in curly brackets. Sets are unchangeable, meaning you cannot change items of the set
once created. Sets do not contain duplicate items.
"""

s = {2,4,2,4}
print(s) 
#output - {2, 4} set doesn't contain duplicate values


# set is unorderd 
info = {"Carla", 19, False, 5.9, 19}
print(info)
#output-  {'Carla', False, 19, 5.9}

# sets = set()
# print(type(sets))

#Accessing set items
for value in info:
    print(value)
    
# Exercise
 
def common_elements(list1, list2):
    common = set()                 #defining empty set
    for elements in list1:
        if elements in list2:
            common.add(elements)
            
    return common

list1 = [1,3,6,7,8,2]
list2 = [11,2,6,12,20,8]

print(common_elements(list1,list2))
#output {8,2,6}

