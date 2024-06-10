# Dictionary Methods 
# Dictionary uses several built-in methods for manipulation. They are listed below

info = {
    "emp_name": "Mahesh",
    "emp_id": 9911,
    "job": "Clerk",
    "salary": 12000   
}

# update()
# The update() method updates the value of the key provided to it if the item already exists in the dictionary,
# else it creates a new key-value pair.
info.update({'DOB': 2001}) 
info.update({"salary": 13000})
print("After update:", info)

# clear()
# The clear() method removes all the items from the dictionary.
randommm = {
    12: 21212,
    21: 231313
}
randommm.clear()
print("After clear:", randommm)  # {}

# pop()
# The pop() method removes the key-value pair whose key is passed as a parameter.
info.pop('DOB')
print("After pop('DOB'):", info)  # {'emp_name': 'Mahesh', 'emp_id': 9911, 'job': 'Clerk', 'salary': 13000}

# del()
# The del statement removes the item with the specified key.
del info["emp_id"]
print("After del info['emp_id']:", info)  # {'emp_name': 'Mahesh', 'job': 'Clerk', 'salary': 13000}

# copy()
# The copy() method returns a shallow copy of the dictionary.
info_copy = info.copy()
print("Copy of info:", info_copy)

# fromkeys()
# The fromkeys() method creates a new dictionary with keys from the given sequence and values set to the provided value.
keys = ['a', 'b', 'c']
value = 1
new_dict = dict.fromkeys(keys, value)
print("Dictionary from keys:", new_dict)

# get()
# The get() method returns the value for the specified key if key is in the dictionary, else default.
salary = info.get('salary')
print("Get salary:", salary)
non_existent = info.get('non_existent', 'default_value')
print("Get non-existent key:", non_existent)

# items()
# The items() method returns a view object displaying a list of dictionary's key-value tuple pairs.
items = info.items()
print("Items:", items)

# keys()
# The keys() method returns a view object displaying a list of all the keys in the dictionary.
keys = info.keys()
print("Keys:", keys)

# popitem()
# The popitem() method removes and returns an arbitrary (key, value) pair from the dictionary.
key, value = info.popitem()
print("Popitem:", (key, value))
print("After popitem:", info)

# setdefault()
# The setdefault() method returns the value of the specified key. If the key does not exist, inserts the key with the specified value.
default_value = info.setdefault('job', 'Engineer')
print("Set default job:", default_value)
default_value = info.setdefault('emp_id', 9922)
print("Set default emp_id:", default_value)
print("After setdefault:", info)

# values()
# The values() method returns a view object displaying a list of all the values in the dictionary.
values = info.values()
print("Values:", values)

# Iterating over keys
print("Iterating over keys:")
for key in info.keys():
    print(key)

# Iterating over values
print("Iterating over values:")
for value in info.values():
    print(value)

# Iterating over items
print("Iterating over items:")
for key, value in info.items():
    print(f"{key}: {value}")

# Dictionary comprehension
# Creating a dictionary with squares of numbers
squares = {x: x**2 for x in range(6)}
print("Squares dictionary:", squares)
