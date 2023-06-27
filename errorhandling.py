a = input("Enter a number ")
try:
    for i in range(1,11):

        print(f"{int(a)} x {i} = {int(a)*i}")
except:
        print("Invalid input")
