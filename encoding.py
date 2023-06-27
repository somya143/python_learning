inp = input("Enter you input here ")
len = len(inp)
encoding = True
if(encoding):
    if(len>=3):
        dup=inp
        fl=dup[0:1]
        end=dup[1:]+fl
        random= "ion"+end+"jhu"
        print(random)
    else:
        print(inp[::-1])



