name = "Swayam"
for i in name:
  print(i)
  
colors = ["Red","Green","Blue","Yellow","Purple"]
for color in colors:
  print(color)
  for i in color:
      print(i)  

# Range Syntax given below
# range(start: int, stop: int, step: int)

for k in range(5):
    print(k + 1) 
         
# Here we are defining the condition for the loop using range to tell its start and end point.         
for j in range(1,10,2):
    print(j) 

# To skip a no. we can use continue keyword

for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)     

# Break Statement
# What it does is it breaks out of the loop
for i in range (12):
    if(i == 10):
        break
    print("5 X", i, "=", 5 * i)
print("Out of Loop")

# Continue
# Proceed and gives of the data till meet the given instructions
for j in range (12):
    if(j == 10):
        print("Skip The Iteration")
        continue
    print("5 X", j, "=", 5 * j)
