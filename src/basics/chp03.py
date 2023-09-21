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
for x in range(0, 345+15, 15):
    print(x,"--",round(math.sin(math.radians(x)),4), round(math.cos(math.radians(x)),4))
else:
    print("completed printing the range")

print("Exercise.problem.16 ---------------------")
Y = input("enter a year (format=yyyy): ")

if not Y or not Y.isnumeric() or Y.isspace():
    print("you did not enter year number")
else:
    Y = eval(Y)
    C = Y // 100
    m = (15 + C - (C/4) - ((8 * C + 13)/25)) % 30
    n = (4 + C - (C/4)) % 7
    a = Y % 4
    b = Y % 7
    c = Y % 19
    d = (19 * c + m) % 30
    e = (2 * a + 4 * b + 6 * d + n) % 7
    print("Y:",Y,"C:",C,"m:",m,"n:",n)
    print("a:",a,"b:",b,"c:",c,"d:",d,"e:",e)

    if (d == 29) and (e == 6):
        print("easter falls one week earlier on April 19")
    elif (d == 28) and (e ==6) and m in [2, 5, 10, 13, 16, 21, 24, 39]:
        print("easter falls one week earlier on April 18")
    else:
        print("using march logic ... Mar(22+d+e)")
        m_day = 22 + d + e
        if m_day > 31:
            print("easter falls on Apr:", math.floor(m_day - 31))
        else:
            print("easter falls on Mar:", math.floor(m_day))

        print("or using april logic ... Apr(d+e-9)")
        a_day = d + e - 9
        if a_day < 1:
            print("easter falls on Mar:", math.floor(31 - a_day))
        else:
            print("easter falls on Apr:", math.floor(a_day))


print("Exercise.problem.17 ---------------------")
Y = input("enter a year (format=yyyy): ")

if not Y or not Y.isnumeric() or Y.isspace():
    print("you did not enter year number")
else:
    Y = eval(Y)
    isDivisibleBy4 = (Y % 4 == 0)
    isDivisibleBy100 = (Y % 100 == 0)
    isDivisibleBy400 = (Y % 400 == 0)

    if isDivisibleBy400:
        # for example 2000
        print(Y, "is a Leap Year")
    elif isDivisibleBy100:
        #  for example 1900
        print(Y, "is not a Leap Year")
    elif isDivisibleBy4:
         # for example 2008
        print(Y, "is a Leap Year")
    else:
        print(Y, "is not a Leap Year")


print("Exercise.problem.18 ---------------------")
amt = input("give an amount of change less than $1.00: ")

if not amt or not amt.isnumeric() or amt.isspace():
    print("you did not enter year number")
else:
    amt = eval(amt)
    quarters = amt // 25
    remaining = amt % 25
    dimes = remaining // 10
    remaining = remaining % 10
    nickels = remaining // 5
    pennies = remaining % 5

    print("to make that change, it will need", quarters, "quaters", dimes, "dimes",nickels,"nickels",pennies,"pennies")

# print("Exercise.problem.19 ---------------------")
