#seek() and tell() function
""" 
In Python, the seek() and tell() functions are used to work with file object and their positions within a file. These functions are part of the buit-in io module, which
provides consistent interface for reading and writing to various file-like objects , such as files, pipes, and in-memory buffers.

seek()function
The seek() function allows you to move the current position within  a file to specific point. The position is specified in bytes, and you can move 
either forward or bacjward from the current position.

tell() function
The tell() function returns the current position within the file, in bytes. This can be useful for keeping track of your location within the file or for seeking
to a specific position relative to the current position.

truncate() function
When you open a file in Python using open function, you can specify the mode in which you want to open the file. If you specify the mode as 'w'
or 'a' the file is opened in a write mode and you can write to the file. However, if you want to truncate the file to a specific size, you can use the truncate function.
"""
#seek() function
with open('myfile.txt','r') as f:
   print(type(f))
   f.seek(10)           # move to the 10th byte in the file
   data = f.read(5)     # read the next 5 bytes
   print(data)
   
    
#tell() function
with open('myfile.txt','r') as f:
    data = f.read(10)               # read the first 10 bytes
    current_postion = f.tell()      # Save the current position
    print(f.seek(current_postion))  # seek to the saved postion
    
#truncate() function
with open('demo.txt','w') as f:
    f.write("Hello World!!")
    f.truncate(5)
    
with open('demo.txt','r') as f:
    print(f.read())                    # Output - Hello
