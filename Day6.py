#Type casting 
''' Conversion of one data type into another data type is known as typecasting
pyyhon supports variety of methods or function like str(), int(), float(),list(),dict() etc for type casting.
Explicit typecasting: Conversion done by developer. 
'''
number = 12
string = '3'
strToint = int(string)
sum = number + strToint
print(sum)

'''Implicit typecasting: One data type is converted into another data type by python interpreter itself.
   python convert smaller data type  into higher data type to prevent data loss. 
'''
floats = 8.8
integers = 1
sum1 = floats + integers
print(sum1)
print(type(sum1))
#output converts integer to float when we add both of the data type together 
