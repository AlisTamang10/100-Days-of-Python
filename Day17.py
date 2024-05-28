# Function
""" 
A function is a block of code that peroforms a sepecific task whenerver it is called.
In bigger programs , where we have large amounts of code, it is advisable to create or use
existing functions that make the program flow organized and neat.
There are two tpes of functions:
1. Built in functions
2. User-defined 

"""
#userdefine function

def isGreater(a,b):
    
    if (a >b):
        print("First number is greater.")
    else:
        print("Second number  greater or equal.")
        
        
a = 5
b = 3
isGreater(a,b) # calling function and passing arguments
isGreater(7,9)

import random

def rock_paper_scissors():
    choices = ['rock','paper','scissor']
    computer_choice = random.choice(choices)
    user_choice = input("Enter you choice: ").lower()
    
    print("Computer choice is: ",computer_choice)
    
    if user_choice == computer_choice:
        print("------- GAME TIE-------")
    elif (user_choice == 'rock' and computer_choice == 'scissor') or (user_choice == 'paper' and computer_choice == 'rock') or \
        (user_choice== 'scissor' and computer_choice == 'paper'):
            print("----------YOU WIN---------")
            
    else:
        print('-----------YOU LOSE----------')
        
rock_paper_scissors()