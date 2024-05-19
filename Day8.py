# Strings
"""
In python anything enclose between single or double quotation mark is considered as string.
String is essentially sequence or arrays of textual data.    
"""
# Example
string = 'Hello Its alis '
string1 = " Sup "
print(string,string1)

# Multi Line strings
#Example 
a = '''
In the heart of the bustling city, nestled between towering skyscrapers, there was a quaint little bookstore called "Whispers of the Past." 
The store was owned by an elderly man named Mr. Thompson, whose silver hair and kind eyes spoke of a thousand untold stories. 
'''
print(type(a),a)

# Accessing Charecters of string
print(string[0],string[1],string[2])

#Looping through the strings

for chars in string:
    print(chars)