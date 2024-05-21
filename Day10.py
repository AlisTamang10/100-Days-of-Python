# String Methods
#Python provides a set of built in methods that we can use tp after and modify the strings.

# Strings are immutable
nm = "Alis"
print(len(nm))

print(nm.upper())
print(nm.lower())

#rstrip()
a = "hellooo !!!!"
print(a.rstrip('!')) #removes exclamatory sign

#replace()
#The replcae method replaces all occurances of a string with another string.

str1 = "Silver Spoon"
print(str1.replace("Spoon", "Moon"))

#Capitalize()
#The capitalize() method turns only the first character of the string to the uppercase.

str2 = "hola amigo"
print(str2.capitalize())

#center
#The center method aligns the string to the center as per the parameter given by the user.

str0 = "Welcomemates"
print(str0.center(50))
#count
print(str1.count('S'))
#find

str1 = "The center method aligns the string to the center as per the parameter given by the user."
print(str1.find("aligns"))

#isalnum
#The isalnum() method returns True only if the entire string only conssits of A-Z,a-z,0-9,
#If any other characters or puctuations are present, then it returns False.
print(str0.isalnum())
print(str0.isalpha())

#islowercase()
b = "lowercase\n"
print(b.islower())

#isprintable()
print(b.isprintable()) #string contains \n which is not printable

#title()
print(str2.title())

#isspace
c= "   "
print(c.isspace()) # check if the string contains space or not

#swapcase()
d = "UPPERCASE"
print(d.swapcase()) # swaps lower to the upper an vice versa
