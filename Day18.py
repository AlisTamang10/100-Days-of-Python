# Function Arguments and return statements
""" 
There are four types of arguments that we can provide in a function
- Default arguments
- Keyword Arguments
- Variable length arguments
- Required Arguments
- Default Arguments:-
 We can provide a default value while creating a function. This way the 
 assumes a default value even if a value is not provided in the function call argument.
"""
#default argument example
def average(a = 10, b=20):
     print("The average is ", (a+b)/2)
   
average(b=10) # making argument a be default argument
   
def name(fname, midname = 'Von', lname='Namgoong'):
    print("Hello",fname,midname,lname)
    
name('Kim') # Except first name others are default argument
''' 
Keyword argument
We can pass the arguments with key = value , this way the interpreter recognizes the arguments by the paramenter name.
Hence, the order in which arguments are passed does not matter.
'''
#For example 
name(fname='Bhakta',midname='Bahadur',lname='Tamang') #Keyword argument
''' 
Required Arguments
In case we don't pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should be match in actual function.
'''
#for example
name(fname="Sameer") #other are optional but we have to pass fname cause its required argument
#Arbitary Arguments
def averaGe(*numbers):
    print(type(numbers))
    sum = 0 
    for i in numbers:
        sum = sum + i
    print('Average value of numbers is:', sum/len(numbers))
    
averaGe(5,45,3,4,7) # *args takes the arguments as tuple

# Keyword Arbitary Arguments
def info(**detail):
    print(type(detail))
    print('Details Are:',detail["fname"],detail['lname'],detail['Age'],detail['Job'])
info(fname= 'Alis',lname='Tamang',Age= 18,Job ='Student') #**args takes arguments as dictionary