#Python - else in Loop
""" 
As you have learned beofre, the else clause is used along with the if statement.
Python allows the else keyword to be used with the for and while loops too. The else 
block appears after the body of the loop. The statements in the else block will be executed after all iterations
are completed. The program exits the loop after the else block is executed.
 """
 
for i in range(5):
    print(i)
    if i==4:
        break
else:
    print("Sorry no i") 
    

i = 0
while i<7:
    print(i)
    i = i + 1
else:
    print("Sorry no i")
  
    
for x in range(5):
    print("iteran no {} in for loop".format(x+1))
else:
    print("else block in loop")
print("Out of the loop")