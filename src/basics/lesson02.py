import math

sec = input("give me number of seconds ")

if not sec:
    print("the input is blank !!", sec)

elif sec.isnumeric() :
    min = eval(sec) // 60;
    remaining_sec = eval(sec) % 60

    print("you gave", min, "minutes", remaining_sec, "seconds")
else :
    print("the input is not numeric",sec)

# print("you gave", (sec//60), "minutes", (sec%60), "seconds")
# ----------------------------

hour = input("Enter hour: ")
hrs_ahead = input("How many hours ahead?")

total_hrs = eval(hour) + eval(hrs_ahead)
hrs_after12 = total_hrs % 12
print("New hour:",hrs_after12,"o'clock")
