# If else statement
"""
Sometimes the programmer needs to check the evalutation of certain expressions(s),
whether the expression(s) evaluate to Ture or False.
If the expression evaluates to False, then the program execution follows a 
different path than it would have if the expression had evaluated to True
Based on this, the coditional statements are further classified into following types
- if
- if else
- if elif else
- nested if else elif
"""
# Conditional Operators
# >,<, >=,<=, ==, !=

a = int(input("Enter your age: "))
print("Your age is:", a)

if a > 18:
    print("You can drive")
    
else:
    print("You can not drive")
    
    
apple_price = 10
budget = 200

if (budget - apple_price > 50):
    print("Alexa, add 1 kg apple to cart")
    
elif (budget - apple_price >70):
    print("Alexa, you can buy it") 
else:
    print("Alexa, do not add apple on the cart.")
    
num = int(input('Enter the number: '))

if num < 0:
    print("Number is negative")
elif num == 0:
    print("Number is zero")
elif num == 999:
    print("Number is special")
else:
    print("Number is positive")
    
#Nested if statement

nums = 0

if nums < 0:
    print("Number is negative")
elif nums > 0:
    if nums < 10:
        print("Number is in between 1 - 10")
    elif (nums > 10 and nums< 20):
        print("Number is in between 10 - 20")
    else:
        print("Number is greater than 20")
        
else:
    print("Number is zero")