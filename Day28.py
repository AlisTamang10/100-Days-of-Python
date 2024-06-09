#python dictionaries 
"""
Dictionaries are ordered collection of data items. They store multiple items in a single variable.
Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets{}.
 
"""
dict = {
    "Name": "Alis",
    "Age" : 21,
    "Nationality" : "Nepalese"
    
}
print(dict)

# Accesing dictionaries
# Value in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets 
# or by using get method

print(dict["Name"])
print(dict.get("Age2")) # returns None 

# Accessing multiple values
print(dict.values())
print(dict.keys())

for key in dict.keys():
    print(f"The value corresponds to the key {key} is {dict[key]}")

#Accessing key value pairs
print(dict.items())
for key,value in dict.items():
    print(f"{key} ----> {value}")

    
