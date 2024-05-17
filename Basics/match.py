a = int(input("Enter the number :"))
match a:
    case 0:
        print(a,"is equals to zero")
    case 1:
        print(a,"is equals to one")
    case 2:
        print(a,"is equals to two")
    case _ if a!=0:
        print(a,"is not equals to zero")
    case _ if a!=1:
        print(a,"is not equals to one")
    case _:
        print(a)                