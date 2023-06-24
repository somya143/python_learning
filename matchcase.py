i = int(input("Enter a number: "))

match i:
    case 0:
        print("print 0")
    case 1:
        print("print 1")
    case 2:
        print("print 2")
    case _:
        print(i)