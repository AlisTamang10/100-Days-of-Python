#readlines() method
# The read line method reads a single line from the file. If we want to read multiple lines, we can use a loop.
# The writelines() method in Python writes a sequence can be any iterable object, such as a list or tuple.
# f = open('demo.txt', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# Readlines()
f = open('demo.txt', 'r')
i = 0
while True:
    i = i+1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(',')[0])
    m2 = int(line.split(',')[1])
    m3 = int(line.split(',')[2])
    print(f"Marks of student {i} in Maths is: {m1}")
    print(f"Marks of student {i} in Scicene is: {m2}")
    print(f"Marks of student {i} in CS is: {m3}")
    print(line)

    
# Writelines
f = open('myfile.txt','w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()

# for loop to add lines
f = open('myfile.txt', 'w')
lines = ['line 1','line 2', 'line 3', 'line 4']
for line in lines:
    f.write(line + '\n')
f.close()