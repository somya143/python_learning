inp = input("Enter you input here ")
len = len(inp)
decoding = True

if(decoding):
    if(len<3):
        print(inp[::-1])
    else:
        random=inp[3:-3]
        #ll=random[-1]
        newStr=random[-1]+random[:-1]
        print(newStr)