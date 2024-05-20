#Strings Slicing and Operations on Strings
# we can find the length of the string by len() function.

# Slicing through strings

name = "Alis Tamang"
slices = name[0:4]
print(slices)

Fruit = "Mango"
MangoLen = len(Fruit)
print(MangoLen)
print(Fruit[0:4]) #including 0 but not 4
print(Fruit[1:4])
print(Fruit[0:]) #slicing till end
print(Fruit[:5]) #Slicing from start
print(Fruit[0:-3]) #slicing using negative index
print(Fruit[0:len(Fruit)-3])
print(Fruit[-3:-1])

# Quick Quiz 
nm = "Harry"
print(nm[-4:-2]) #ans ar

