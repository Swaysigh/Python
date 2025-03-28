info = {"SWAYAM",False,5.9, 19}
print(info)
#unordered collection of data items.

for value in info:
    print(value)
# Here the output will always be random because of set being unordered Collection of Data

# Empty set if declared Loosly can create a Dictionary instead of a Set
swayam=set()
print(type(swayam))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Toky")
print(cities)