import random
#Break and Continue
#Break Statement
"""
The break statement enables a program to skip over a part of the code.
A break statement terminates the very loop it lies within. 
"""
for i in range(12):
    print("5 X ", i, "=", 5 * (i))
    if (i == 10):
        break 
print("Out of the loop")

# Continue Statement
# The continue statement skips the rest of the loop statements and cuases the 
# next iteration to occur.

for i in range(12):
    if (i == 10):
        print("Skip the iteration")
        continue
    print("5 X ", i ,"=", i * 5)
    

correct_number = random.randint(1, 10)
print("Welcome to guessing game")
print("Guess number between 1 to 10, If you geuss number 5 , Game will end. ")

while True:
    guess = int(input("Enter your guess number: "))
    if guess == 5:
        print("----------GAME END----------")
        break # using break statement
    
    if guess%2 != 0:
        print("You choose odd number, Try Again !!")
        continue
    
    if guess == correct_number:
        print("Congrats !!, You won the game")
        break
    else:
        print("That's not the correct number, Try Again!")
        
