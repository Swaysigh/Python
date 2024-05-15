import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
if (timestamp >= '04:00:00' and timestamp < '12:00:00'):
    print("Good morning")
elif (timestamp >= '12:00:00' and timestamp < '17:00:00'):
    print("Good Afternoon")
elif (timestamp >= '17:00:00' and timestamp < '21:00:00'):
    print("Good Evening")
elif (timestamp >= '21:00:00' or timestamp < '04:00:00'): 
    print("Good Night")
else:
    print("Error: Invalid time range")