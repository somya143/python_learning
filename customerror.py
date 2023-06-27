a = int(input("Enter a number between 1 to 9 "))

if(a<1 or a>9):
    raise ValueError('Number should be between 1 to 9')
elif(a == "quit"):
    raise TypeError("This is exception")
else:
    raise TypeError("This is not a number but a string. Number expected")