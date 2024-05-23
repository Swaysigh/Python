# Lists are ordered Collection of data items
# Its Mutable
arr = [1 , 6 , 3]
print(arr)

# Its can store all data types
marks = [1 , 5 , "marks" , False , 55 , 99]
print(marks[0])

# We can use if else as well
if 5 in marks:
    print("Yes")
else:
    print("No")

# We can perform string slicing here as well
print(marks[1:5])

# We can use constraints inside a list
list = [i*i for i in range(10) if i % 2 == 0]
print(list)

# Some methods to edit list
l = [11 , 25 , 6 , 74 , 31 , 3]

# Adds a given element at the end of list
l.append(5)

# Sorts the list in ascending order
l.sort()

# Sorts the list in descending order
l.sort(reverse=true)

# Arranges the given list in Reverse
l.reverse()

# Tells the index of given Element
print(l.index(3))

# Counts the no. of times the element is present in the list
print(l.count(6))   

# Creates a Copy of List
m = l.copy() 

# The first parameter tells us about the index while the other is the element which going in that index
l.insert(1,88)

# What's happening here is that the elements of j are merged at the last of list l
j = [25 , 6 , 33]
l.extend(j)

# Another way of Concatenation
k = l + j
print(k)