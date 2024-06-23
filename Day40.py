#Opening a file 
""" 
Before we can perform any operations on a file, we must first open it. Python provides the open() function to open a file. It takes to arguments: the name of the file and
the mode in which the file should be opened. The mode can be 'r' for reading. 'w' for write or 'a' for appending.
Modes in file
read(r)- this mode opens the file for reading only and gives an error if the file doesnot exist. This the default mode if no mode is passed as parameter.
write(w)- This mode opens the file for writing only and creates a new file if the file doesnot exist.
append(a)- This mode opens the file for appending only and creates a new file if the file doesnot exist.
create(x)- This mode creates a file and gives an error if file already exist.
text(t)- Apart from these modes we also need specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since 
the text mode is default . The default mode is 'r' (open for reading textm synonym of 'rt)
"""
# Writing to a file
f = open('demo.txt','w')
f.write("Hello it's me.")
f.close()

# Appending to a file
f = open('demo.txt','a')
f.write("Alis Tamang")
f.close

# Reading File
f = open('demo.txt', 'r')
text = f.read()
print(text)
f.close()         #output - Hello it's me.Alis Tamang

# The With statement
# Alternatively, you can use th with statement to automatically close the file after you are done with it.

with open('demo.txt','r') as f:
    txt = f.read()
    print(txt)