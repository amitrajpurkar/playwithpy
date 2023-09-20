import math

print("Book: a practical introduction to python programming -- by: Brian Heinold")
print("Welcome to chapter 3")


print("Exercise.problem.08 ---------------------")

sec = input("give me number of seconds: ")

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

print("Exercise.problem.09 ---------------------")

hour = input("Enter hour: ")
hrs_ahead = input("How many hours ahead? ")

if hour.isnumeric() and hrs_ahead.isnumeric():
  total_hrs = eval(hour) + eval(hrs_ahead)
  hrs_after12 = total_hrs % 12
  print("New hour:",hrs_after12,"o'clock")
else:
    print("one of the inputs was not numeric",hour,hrs_ahead)

print("Exercise.problem.10 ---------------------")
pow = input("enter a number for power of 2: ")
dig = input("enter how many last digits you want: ")
if pow.isnumeric() and dig.isnumeric():
    calc_num = math.pow(2, eval(pow))
    last_digit = calc_num % 10
    print("last digit of 2 to the power", pow, "is",last_digit)
    last_2dig = calc_num % 100
    print("last two digits of 2 to the power", pow, "are", last_2dig)
    last_n = calc_num % (math.pow(10,eval(dig)))
    print("last n digits of 2 to the power", pow, "are", last_n)
else:
    print("Shazaam !! the entered power is not numeric",pow)

print("Exercise.problem.11 ---------------------")
wt = input("enter weight in kilograms: ")
wt_num = eval(wt) if wt.isnumeric() else 0
if wt_num == 0:
    print("verify is weight provided is numeric:",wt)
else :
    wt_pnd = round(wt_num * 2.20462, 1)
    print("the weight in pounds is:",wt_pnd)


print("Exercise.problem.12 ---------------------")
num = input("give me a number: ")
if not num.isnumeric():
    print("you did not give numeric value !!",num)
else:
    fac = math.factorial(eval(num))
    print("factorial of",num,"is",fac)

print("Exercise.problem.13 ---------------------")
num = input("give me a number: ")
if not num.isnumeric():
    print("you did not give numeric value !!",num)
else:
    print("sine value of",num,"is",math.sin(eval(num)))
    print("cosine value of",num,"is",math.cos(eval(num)))
    print("tangent value of",num,"is",math.tan(eval(num)))


print("Exercise.problem.14 ---------------------")
num = input("give an angle in degrees: ")
if not num.isnumeric():
    print("you did not give numeric value !!",num)
else:
    print("sine value of",num,"degrees is",math.sin(math.radians(eval(num))))


print("Exercise.problem.15 ---------------------")
