#os module in python
"""
The os module in Python is a built-in library that provides functions for interacting with the operating system. It allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the fily system, and running system commands.

"""
import os
if (not os.path.exists()):
    os.mkdir("data")

for i in range(0,100):
    os.makedir(f"data/Day{i+1}")
    
#rename

for i in range(0,100):
    os.rename(f"data/Tutorial{i+1}",f"data/Tutorial {i+1}")
    
#os list
folders = os.listdir("data")

for folder in folders:
    print(os.listdir(folders))