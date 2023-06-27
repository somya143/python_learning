try:
    for i in range(5):
        print(int(input("Enter a number")))
except:
    print("Invalid input")

finally:
    print("I will always get executed")#