# Finally Keyword
""" 
The Finally code block is also a part of exception handling. When we handle exception using the try and except block, we can
include a finally block at the end. The finally block is always executed, so it is generally used for doing the conluding tasks like 
closing file resources or closing database connection or may be ending the program execution with a 
delightful message.
"""

try:
    l = [1,4,6,7,9]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("some error occured !!")
finally:
    print("I am always executed.")
    
#use of finally keyword in function
    
def division(a,b):
    
    try:
        result = a/b
        return result
    
    except ZeroDivisionError:
        return "Can not divided by zero."
    
    finally:
        print("I am always executed....")
        
display = division(4,0)
print(display)
        

    
    