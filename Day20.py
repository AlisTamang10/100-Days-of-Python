#List Methods
#Python List Methods are the built-in methods in lists used to perform operations on Python lists/arrays.

nums = [1,2,3,5,8,9]
fruits = ["Pineapple","Watermelon","Apple","Banana","Mango"]

#list.append()
#Used for adding elements to the end of the list
nums.append(10)
fruits.append("Sugarcane")

#list.sort()
# This method sorts the list in ascending order.
fruits.sort()
nums.sort()
print(fruits)
print(nums)

#list.reverse()
#This method reverse the order of the list
fruits.reverse()
nums.reverse()
print(fruits)
print(nums)

#list.index()
print(fruits.index("Apple"))

#list.copy()
#Returns copy of the list. This can be done to perform operations on list without modifying the org list.
newList = nums.copy()
print(newList)

#insert()
# THis method inserts an item at the given index. User has to specify index and the item to be iserted within the insert() method.
fruits.insert(1,'Grape')
print(fruits)

#extend()
# This method add an entire list or any collection datatype(set, tuple, dictionary) to the existing list.
fruits.extend(nums)
print(fruits)   #output - ['Watermelon', 'Grape', 'Pineapple', 'Mango', 'Banana', 'Apple', 9, 8, 5, 3, 2, 1]

#remove()
#Removes specific element
fruits.remove("Sugarcane")
print(fruits)