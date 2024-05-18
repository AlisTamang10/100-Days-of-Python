# Taking User inputs
'''
In python , we can take user input by using input function(),
it returns strings value/ characters. 
For Example 
'''
in1 = input("Enter something: ")
print(type(in1))
# There we have to do type casting when taking input as per the preferences
# For Example 
in2 = int(input('Enter numbers: '))
print(type(in2))

#Exercise 
num1 = int(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#Arithmetic Operations
sums = num1 + num2
mul = num2 * num1
sub = num1 - num2
div = num1 / num2

print('sum of num1 and num2', sums)
print('multiplication of num1 and num2', mul)
print('subtraction of num1 and num2', sub)
print('division of two numbers', div)

