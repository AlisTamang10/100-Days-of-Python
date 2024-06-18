#Enumerate Function
""" 
The enumerate function is a built-in function in Python that allows you to loop over a sequence(such as a list, tuple, or string)
and get the index and value of each element in the sequence at the same time.

"""
marks = [77,66,54,68,64]
index = 0
for mark in marks:
    print(mark)
    if (index == 2):
        print("Average")
    index += 1

# if we use enumerate function
for index, mark in enumerate(marks):
    print(mark)
    if (index == 2):
        print("Your marks is average.")

#example 
fruits = ['apple','guava','pineapple','watermelon']

for index,fruit in enumerate(fruits):
    print(index,fruit)

#output
"""
0 apple
1 guava
2 pineapple
3 watermelon 
"""
#Changing the start index
for index,fruit in enumerate(fruits, start=1):
    print(index,fruit)
    
#output
"""
1 apple
2 guava
3 pineapple
4 watermelon
"""
# Exercise : Write a program to filter out elements from a list where the index is not a multiple of 3.
data = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for index, nums in enumerate(data):
    if index % 3 == 0:
        print(f"{nums}")
        
    
        

