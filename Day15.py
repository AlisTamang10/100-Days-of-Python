#While Loop 
""" 
As the name suggests, while loops execute statements while the condition is True.
As soon as the condition become False, the interpreter comes out of the while loop.
"""
# Else with While loop
""" 
We can even use the else statement with the while loop. Essentially what the else statement
does is that as soon as the while loop condition becomes False, the interpreter comes out of the 
while loop and the else statement is executed. 
"""
# increamenting loop
i = 0
while(i<3):
    print(i)
    i = i + 1
print("done with the loop")    

#decreamenting loop
# Else with While loop
count = 5
while (count > 0):
    print(count)
    count = count - 1
    
else:
    print("I am inside else")   
# Making some patterns

i = 0

while i < 5:
    print(i * "*")
    i = i + 1
    
height = 5
row = 0

while row < height:
    spaces = height - row - 1
    stars = row + 1
    print(' ' * spaces + '*' * stars)
    row += 1




    