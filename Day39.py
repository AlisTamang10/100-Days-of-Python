# Local vs Global Varaible
""" 
A local variable is a variable that is defined within a function and is only acessible within that function.
It is created when the function is called and is destroyed when the function returns.

On the other hand, a global variable is a variable that is defined outside of a function and is accessible form 
within any function in your code.

The global keyword is used to declare that a variable is a global variable and should be accessed from global scope.
"""
var = "hello"                               #global variable

def variables():
    var = 'hi'                              #local variable
    print(f"This is local variable {var}")
    
print(f"This is global variable {var}")
variables()
print(f"This is global variable {var}")


#global keyword


x = 10             #global variable

def my_func():
    global x
    x = 5    #this will change the value of global variable x
    y = 9    #local variable
    print(y)

my_func() #output 9
print(x)  #output 5

    