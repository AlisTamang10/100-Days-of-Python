# Sets methods
#Joining sets
# Sets in python more or less work in the same way as sets in mathematics. We can perform operations like 
#union and intersection on the stets just like in mathematics.

# union() and update()
""" The union() methods prints all items that are present in the two sets. The union() method
returns a new set wheareas update() method adds item into the existing set from another set."""

s1 = {1,2,3,4}
s2 = {5,6,7,8,9}
print(s1.union(s2))
#output - {1, 2, 3, 4, 5, 6, 7, 8, 9}
cities= {"Tokyo","Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo","Seoul" ," Kabul", "Madrid"}
unionOf2cities = cities.union(cities2)
print(unionOf2cities)

s1.update(s2)
print(s1,s2)
#output - {1, 2, 3, 4, 5, 6, 7, 8, 9} {5, 6, 7, 8, 9}

#intersection and intersection_update
""" The intersection and intersection_update() methods prints only items that are similar to both the sets. The intentsection method returns
a new set whereas intersection_update() method updates into the existing set from another set"""

intersetcionOf2cities = cities.intersection(cities2)
print(intersetcionOf2cities)
#output - {'Madrid', 'Tokyo'}

#intesection_update()
cities.intersection_update(cities2)
print(cities)
#output - {'Madrid', 'Tokyo'}

#symmetric_difference()

symmetricDifCities = cities.symmetric_difference(cities2)
print(symmetricDifCities)
#output -{'Seoul', ' Kabul'}

#symmetric_diiference_update
cities.symmetric_difference_update(cities2)
print(cities)

#isdisjoint()
# The isdisjoint() method checks if items of given set are present in another set are present in 
# another set. This method returns False if items are present, else it returns True. 

cities1 = {"Tokyo1","Madrid", "Berlin", "Delhi"}
cities3 = {"Tokyo","Seoul" ," Kabul", "Madrid1"}
print(cities1.isdisjoint(cities3)) #True

#issuperset()
# The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.
cities4 = {"Seoul" ," Kabul"}
print(cities3.issuperset(cities4)) #True

#issubset()
#The issubset() method checks if all the items of the original set are prsent in the particular set. It return True if all the items are present, else it returns False.
subset = cities4.issubset(cities3)
print(subset)  #True

#add()

cities4.add("Helsinki")
print(cities4) #{' Kabul', 'Seoul', 'Helsinki'}

#update()
# if you want to add more than one item, simply create another set or any other iterable object (list, tuple) and use the updaet() method to add in existing set

s3 = {1,2,3,4,5}
s4 = {7,8,9}
s3.update(s4)
print(s3)     #{1, 2, 3, 4, 5, 7, 8, 9}

#remove / discard
#remove method throws an error when item is not present in the set
s3.remove(9)
print(s3) #{1, 2, 3, 4, 5, 7, 8}

#discard method doesn't throws any error even if the item is not present in the set
s3.discard(8)
print(s3)  #{1, 2, 3, 4, 5, 7}

#del() - deletes an entire set

del s3
print(s3) #throws error

#clear()
s4.clear()
print(s4) # prints an empty set