name=["mohan","sonu","ram","kishan","ramesh",9]

lst=[item for item in name if (len(item)>4)]
print(lst)

name=["mohan","sonu","ram","kishan","ramesh",9]
if 9 in name:
    print("yes")
else:
    print("no")

x="harry is cool"
if "cool" in x:
    print("HARRY IS PRESENT")
else:
    print("HARRY IS NOT PRESENT")  

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)

colors = ["voilet", "indigo", "blue"]
hello=["ram","girish","ramesh"]
colors.append(hello)
print(colors)
colors.insert(3,"ram")
print(colors)

#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)

colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)