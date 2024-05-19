name = "Swayam Singh"
print(len(name))
print(name[0:7])
print(name[9:11])
print(name[0:-3])

print(name[-4:-2])
# What's happening is that it deduces the no. from len of string
# Example [-4:-2] it implies that 12 - 4 = 8 & 12 - 2 = 10
# The code will run from name[8:10]

                         """string functions"""
a = "Hello"
print(a.upper())        #converts str into upper case

print(a.lower())        #converts str into lower case

a = "****Swayam!!!!!"
print(a.strip("*!"))    #removes the characters passed in arguments

a = "hello swayam"
print(a.replace("hello","goodmorning"))     #replaces the string with another string

print(a.split(" "))      #splits the characters after space

print(a.capitalize())    #capitalize the first letter

print(a.center(50))      #shifts the str into center

print(a.count("a"))      #returns the no.of times a character used

a = "!!!!!swayam!!!!!"
print(a.endswith("!",1,4))   #returns bool value if str ends with given argument

a = "he is a good man"
print(a.find("is"))       #returns the index of argument passed

a="hello2222"   
print(a.isalnum())        #returns bool value if str contains A-Z/a-z/0-9 only

print(a.isalpha())        #returns bool value if str contains A-Z/a-z only

print(a.islower())        #returns bool value if str contains only lower case char

print(a.isprintable())    #returns bool value if str contains printable char only

print(a.isspace())        #returns bool value if str contains wide spaces only
 
str1 = "World Health Organization" 
print(str1.istitle())     #returns bool value if first letter of each word is capitalize

print(str1.isupper())     #returns bool value if str contains upper char only

str1 = "Python is a Interpreted Language"   
print(str1.startswith("Python"))          #checks if the string starts with a given value

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())                    #lower case to upper case and vice versa

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())                       #capitalize the first letter of each word
