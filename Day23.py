#f-strings
#String Formatting in python
# String formatting can be done in python using the format method
txt = "For only {price:.2f} dollars"
print(txt.format(price = 49.35953647))
letter = "Hey my name is {}, I am from {}"
country = "Nepal"
Name = "Alis"
print(letter.format(Name,country))


""" 
f- strings in python 
It is a new string formatting mechanism intoduced by the PEP 498. It is alson known as Literal String Interpolation or more commonly as F-string (f charachter preceding the string literal).
The primary focus of this mechanism is yo make the interpoalation easier. When we prefix the string withe the letter"f", the string become the f-string iteself. The f-string can be the formatted
in much same as the str.format() method. The f-string offers a convenient wat to embed Python expression inside string literal for formatting.
"""
#using f string 
print(f"Hey my name is {Name}, Im from {country}")
price = 49.35953647
print(f"For only {price:.2f} dollars")
print(f"We can also use like this: Hey my name is{{Name}}, Im from {{country}}")


# Some Exercises
#Create a program that prints a simple table of squares and cubes for numbers 1 through 10 using f-strings.

print(f"{'Number':<10}{'Square':<10}{'Cube':<10}") #:<10 works as space or padding

for i in range(1,10):
    print(f"{i:<10}{i**2:<10}{i**3:<10}")
    
#Create a program that calculates the percentage of marks obtained by a student and prints it with appropriate formatting.
marks_obtained = float(input("Enter the marks you obtained: "))
total_marks = float(input("Enter the total marks: "))
percentage = (marks_obtained/total_marks) * 100

print(f"Marks Obtained: {marks_obtained}/{total_marks}")
print(f"Total Percentage:{percentage:.2f}%")


