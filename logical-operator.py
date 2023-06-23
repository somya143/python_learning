print(3>2 or 2>3) #this is or operator and will return true if only one condition is also true
print(3>2 and 2>3) #this is and operator and will return true only if both the conditions are true else will return false
print(not 2>3) #this is not or negation operator and will return true if the condition is not true
age=12
if age>18:
    print("You are an adult")
elif age>=13 and age<=19:
    print("You are a teenage")
else:
    print("You are a child")
    #this is if , else if , else condition