firstNum = input("Enter first number : ")
secNum = input("Enter second number : ")
operators = input("Enter operator : (+,-,/,*,%) : ")

if operators == "+":
    print(int(firstNum) + int(secNum))
elif operators == "-":
    print(int(firstNum) - int(secNum))
elif operators == "/":
    print(int(firstNum) / int(secNum))
elif operators == "*":
    print(int(firstNum) * int(secNum))
elif operators == "%":
    print(int(firstNum) % int(secNum))
