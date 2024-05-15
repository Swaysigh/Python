     #If\Else\Elif statement :

age = int(input("Enter the age :"))
if(age>18):
    print("Person can vote")
elif(age==18):
    print("person is a adult")
else:
    print("person is a child and cannot vote")

    #Nested If-Else statement :

num = int(input("Enter Your Number: "))
if(num < 0):
    print("Number is negative")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1-10") 
    elif(num > 10 and num <= 50):
        print("Number is between 11-50")    
    else:
        print("Number is  Greater than 50")        
else:
    print("Number is greater than zero")  


