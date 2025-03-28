x = int(input("ENTER THE NUMBER :"))

match x:
    case 0 :
        print("the no. is zero")
    case 3 if x>0:
        print("the no is positive")
    case _ if x<0:
        print("the no. is negative")
    case _:
        print(x)