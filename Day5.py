# Operators 
#Arithmetic Operators

'''Create a calculator capable of performing addition, subtraction, multiplication and division operations
on two numbers. Output should be readable '''


print("Choose opertions to calculate numbers\n A for Addition \n B for Subtraction \n C for Multiplication \n D for Division")
operation = input("Enter the operation: ")
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

if operation == 'A':
    add = num1 + num2
    print('Addition of two numbers: ', add)
elif operation == 'B':
    sub = num1 - num2
    print('Subtraction of two number:', sub)
elif operation == 'C':
    mul = num1 * num2
    print('Multiplication of two numbers:', mul)
elif operation == 'D':
    div = num1/num2
    print('Division of two numbers:', div)
    