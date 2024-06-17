#Short hand if else 
# There is also a shorthand syntax for the if-else statement that can be use when the condtion being tested is 
# simple and the code blocks to be executed are short. 

# Example 1

a = 330
b = 3303
print("A") if a>b else print("=") if a==b else print("B")

#Example 2

num = 4
option ='even' if num%2 == 0 else 'odd'
print(f"Number {num} is {option}")

#Example 3
age = int(input("Enter your age: "))

classify = "can vote" if age>=18 else "can not vote"
print(f"Your age is {age} and you {classify}.")



# The shorthand syntax can be a convenient way to write simple if-else statements, especially when you want to assign a value to a variable based 
# on a condition. However, it's not suitable for more complex situations where you need to excecute mutiple statements or perform more complex logic. 
# in thos cases, it's best to use the full if-else syntax