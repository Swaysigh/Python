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
