import time 

Current_Time = time.strftime("%H:%M:%S")
Current_Time_Hour = int(time.strftime("%H"))

if (Current_Time_Hour >= 4 and Current_Time_Hour < 12):
    print("Hello Sir, Good Morning. Current time is", Current_Time)
    
elif (Current_Time_Hour >= 12 and Current_Time_Hour < 16):
    print("Hello Sir, Good Afternoon. Current time is", Current_Time)
    
elif (Current_Time_Hour >= 16 and Current_Time_Hour < 22):
    print("Hello Sir, Good Evening. Current time is", Current_Time)
else:
    print("Hello Sir, Good Night. Current time is", Current_Time)
    

