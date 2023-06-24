import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)

if timestamp < "12:00:00" and timestamp >"01:00:00":
    print("It is morning")
elif timestamp > "12:00:00" and timestamp < "17:00:00":
    print("It is afternoon")
elif timestamp > "17:00:00" and timestamp < "24:00:00":
    print("It is evening time")