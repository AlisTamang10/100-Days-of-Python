# if __name__ == 'main' in python
""" 
The if __name__ == 'main' idiom is a common pattern used in Python scriots to determine whether the script is being run directly or being imported as a module into another script.
In Python, the __name__ variable is a built-in variable that is automatically set the name of the current module. When a python script is run directly, the __name__ variable is set to the string 
__main__ when the cript is imported as a module into another script, the __name__ variable is set to the name of the module 
"""
import example_main
example_main.welcome()

def add(x, y):
    """This function adds two numbers"""
    return x + y
def subtract(x, y):
    """This function subtracts two numbers"""
    return x - y
def multiply(x, y):
    """This function multiplies two numbers"""
    return x * y
def divide(x, y):
    """This function divides two numbers"""
    if y == 0:
        return "Error! Division by zero."
    return x / y
def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}") 
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid Input")
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
if __name__ == "__main__":
    main()
