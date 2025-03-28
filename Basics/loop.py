while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break
  
for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")

for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)

for i in range (12):
   print(i)

i = 0
while True:
  print(i)
  i = i + 1
  if(i%100 == 0):
    break

for i in range(12):
  if(i == 10):
    print("Skip the iteration")
    continue
print("5 X", i, "=", 5 * i)

x=min(10,20)
print(x)


for i in range(5):
   print(i)
else:
   print("not in loop")

i=0
while i<=7:
   print(i)
   i+=1
   if i==3:
      break
else:
   print("not in loop anymore")
   