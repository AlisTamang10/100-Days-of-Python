# Wirte a python program to translate a message into secret code language. Use the rules below to translate normal English into code language.
""" 
Coding:
if the word contains atleast 3 charachters, remove the first letter and append it at the end and now
app now append three random characters at the starting and the end.

else:
simply reverse the string

Decoding: 
if the word contains less than 3 characters, reverse it
else:
remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program asks wether you want code or decode
"""
#import modules
import random
import string

strings = input("Enter the message: ")
words = strings.split(" ")
coding = input("Enter the 1 for coding / 0 for decoding: ")
coding = True if (coding == "1") else False

if(coding):
    newstr = []
    for word in words:
        if (len(word))>=3:
            r1 = ''.join(random.choices(string.ascii_letters, k = 3))
            r2 = ''.join(random.choices(string.ascii_letters, k = 3))
            st = r1 + word[1:] + word[0] + r2
            newstr.append(st)
        else:
            st = word[::-1]
            newstr.append(st)
    print(" ".join(newstr))
else:
    newstr = []
    for word in words:
        if (len(word))>=3:
            st1 = word[3:-3]
            st = st1[-1] + st1[:-1]
            newstr.append(st)  
        else:
            st = word[::-1]
            newstr.append(st)
            
    print(" ".join(newstr))
            
