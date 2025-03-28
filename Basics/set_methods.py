cities1={"delhi","madrid","tokyo","hongkong"}
cities2={"newyork","texas","washington","seoul"}

print(cities1.union(cities2))

cities5 = { "Tokyo" , "Barcelona" , "Moscow" , "Delhi"}
cities6 = { "Tokyo" , "Madrid" , "Mumbai" , "Barcelona"}
cities3 = cities5.intersection(cities6)
print(cities3)

print(cities1.isdisjoint(cities2)) #check if given both cities have values in common and returns true and false.

print(cities1.issuperset(cities2)) #checks if city1 contains city2 or not and returns true or false.

print(cities2.issubset(cities1)) #checks if city2 comes under city1 or not and returns true or false.

print(cities1.remove("tokyo")) #raises an error if given item is not available in the set.

print(cities1.discard("seoul")) #doesnot raise an error if given item is not available in set.

print(cities1.add("Mumbai")) #add a value in set.

print(cities1.update(cities2)) #add multiple values.

print(cities1.pop()) #removes last value.

if "madrid" in cities1:
    print("yes")
else:
    print("no")    


del cities1
print(cities1) #entirely removes the set and del is a keyword rather than a method.

cities2.clear() #returns an empty set
print(cities2)