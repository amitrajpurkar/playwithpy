import math

# https://www.brianheinold.net/python/A_Practical_Introduction_to_Python_Programming_Heinold.pdf
print("Book: a practical introduction to python programming -- by: Brian Heinold")
print("Welcome to chapter 3: Numbers")
# https://guicommits.com/organize-python-code-like-a-pro/
# https://stackoverflow.com/questions/37565793/how-to-let-the-user-select-an-input-from-a-finite-list

# Functions and methods should be verbs - function-name should represent an action
def tryout_exercise08():
    print("Exercise.problem.08 ---------------------")

    sec = input("give me number of seconds: ")

    if not sec:
        print("the input is blank !!", sec)
    elif sec.isnumeric():
        min = eval(sec) // 60;
        remaining_sec = eval(sec) % 60
        print("you gave", min, "minutes", remaining_sec, "seconds")
    else:
        print("the input is not numeric", sec)
    pass

def tryout_exercise09():
    print("Exercise.problem.09 ---------------------")

    hour = input("Enter hour: ")
    hrs_ahead = input("How many hours ahead? ")

    if hour.isnumeric() and hrs_ahead.isnumeric():
        total_hrs = eval(hour) + eval(hrs_ahead)
        hrs_after12 = total_hrs % 12
        print("New hour:", hrs_after12, "o'clock")
    else:
        print("one of the inputs was not numeric", hour, hrs_ahead)
    pass


def tryout_exercise10():
    print("Exercise.problem.10 ---------------------")
    pow = input("enter a number for power of 2: ")
    dig = input("enter how many last digits you want: ")
    if pow.isnumeric() and dig.isnumeric():
        calc_num = math.pow(2, eval(pow))
        last_digit = calc_num % 10
        print("last digit of 2 to the power", pow, "is", last_digit)
        last_2dig = calc_num % 100
        print("last two digits of 2 to the power", pow, "are", last_2dig)
        last_n = calc_num % (math.pow(10, eval(dig)))
        print("last n digits of 2 to the power", pow, "are", last_n)
    else:
        print("Shazaam !! the entered power is not numeric", pow)
    pass


def tryout_exercise11():
    print("Exercise.problem.11 ---------------------")
    wt = input("enter weight in kilograms: ")
    wt_num = eval(wt) if wt.isnumeric() else 0
    if wt_num == 0:
        print("verify is weight provided is numeric:", wt)
    else:
        wt_pnd = round(wt_num * 2.20462, 1)
        print("the weight in pounds is:", wt_pnd)
    pass


def tryout_exercise12():
    print("Exercise.problem.12 ---------------------")
    num = input("give me a number: ")
    if not num.isnumeric():
        print("you did not give numeric value !!", num)
    else:
        fac = math.factorial(eval(num))
        print("factorial of", num, "is", fac)
    pass


def tryout_exercise13():
    print("Exercise.problem.13 ---------------------")
    num = input("give me a number: ")
    if not num.isnumeric():
        print("you did not give numeric value !!", num)
    else:
        print("sine value of", num, "is", math.sin(eval(num)))
        print("cosine value of", num, "is", math.cos(eval(num)))
        print("tangent value of", num, "is", math.tan(eval(num)))
    pass


def tryout_exercise14():
    print("Exercise.problem.14 ---------------------")
    num = input("give an angle in degrees: ")
    if not num.isnumeric():
        print("you did not give numeric value !!", num)
    else:
        print("sine value of", num, "degrees is", math.sin(math.radians(eval(num))))
    pass


def tryout_exercise15():
    print("Exercise.problem.15 ---------------------")
    for x in range(0, 345 + 15, 15):
        print(x, "--", round(math.sin(math.radians(x)), 4), round(math.cos(math.radians(x)), 4))
    else:
        print("completed printing the range")
    pass


def tryout_exercise16():
    print("Exercise.problem.16 ---------------------")
    Y = input("enter a year (format=yyyy): ")

    if not Y or not Y.isnumeric() or Y.isspace():
        print("you did not enter year number")
    else:
        Y = eval(Y)
        C = Y // 100
        m = (15 + C - (C / 4) - ((8 * C + 13) / 25)) % 30
        n = (4 + C - (C / 4)) % 7
        a = Y % 4
        b = Y % 7
        c = Y % 19
        d = (19 * c + m) % 30
        e = (2 * a + 4 * b + 6 * d + n) % 7
        print("Y:", Y, "C:", C, "m:", m, "n:", n)
        print("a:", a, "b:", b, "c:", c, "d:", d, "e:", e)

        if (d == 29) and (e == 6):
            print("easter falls one week earlier on April 19")
        elif (d == 28) and (e == 6) and m in [2, 5, 10, 13, 16, 21, 24, 39]:
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
    pass


def tryout_exercise17():
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
    pass

def tryout_exercise18():
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

        print("to make that change, it will need", quarters, "quaters", dimes, "dimes", nickels, "nickels", pennies,
              "pennies")
    pass

def tryout_exercise19():
    # print("Exercise.problem.19 ---------------------")
    pass


# the method/ function below should be treated as single entry method into this script
# it is more like the "public void main() method in java"..
# just that this method is for this specific script --
# for entire module in python we have main.py
def selectFromDict(options, name):
    index = 0
    indexValidList = []
    # problem_needed = input("which exercise do you want to try? ")
    print('Select an ' + name + ':')
    for optionName in options:
        index = index + 1
        indexValidList.extend([options[optionName]])
        print(str(index) + ') ' + optionName)
    inputValid = False
    while not inputValid:
        inputRaw = input(name + ': ')
        inputNo = int(inputRaw) - 1
        if inputNo > -1 and inputNo < len(indexValidList):
            selected = indexValidList[inputNo]
            print('Selected ' +  name + ': ' + str(selected))
            if 8 == selected:
                tryout_exercise08()
            elif 9 == selected:
                tryout_exercise09()
            elif 10 == selected:
                tryout_exercise10()
            elif 11 == selected:
                tryout_exercise11()
            elif 12 == selected:
                tryout_exercise12()
            elif 13 == selected:
                tryout_exercise13()
            elif 14 == selected:
                tryout_exercise14()
            elif 15 == selected:
                tryout_exercise15()
            elif 16 == selected:
                tryout_exercise16()
            elif 17 == selected:
                tryout_exercise17()
            elif 18 == selected:
                tryout_exercise18()
            else:
                print("we dont have this problem ready yet")

            # here call appropriate exercise-function
            retry = input("want to retry? y/n: ").lower()
            if "y" == retry:
                inputValid = False
            else:
                inputValid = True
                break
        else:
            print('Please select a valid ' + name + ' number')
    return selected

# define a dictionary of choices
options = {}
#     [USER OPTION] = PROGRAM RESULT
options['08. Given a number of seconds, give how many minutes and seconds that is'] = 8
options['09. Give and hour and number of hrs, give what will the time in oclock'] = 9
options['10. Given a number, tell last x digits of that number'] = 10
options['11. Given weight in kgs, give the weight in pounds'] = 11
options['12. Given a number, tell the factorial of that'] = 12
options['13. Given a number, tell the sin, cos, tan of that number'] = 13
options['14. Given an angle in degrees, tell sine of that angle'] = 14
options['15. Tell sin, cos of angles from 0 to 345, increments of 15'] = 15
options['16. Given an year, find the date of Easter in that year'] = 16
options['17. Given an year, tell if its a Leap year or not'] = 17
options['18. Given an amount, tell how many quaters, dimes, nickels and pennies'] = 18
options['19. Given height and width, print a modular rectangle'] = 19


# Let user select an exercise
option = selectFromDict(options, 'option')

# https://stackoverflow.com/questions/37565793/how-to-let-the-user-select-an-input-from-a-finite-list
# problem_needed = input("which exercise do you want to try? ")
# match str(selected):
#     case "8":
#         tryout_exercise08()
#     case "9":
#         tryout_exercise09()
#     case "10":
#         tryout_exercise10()
#     case "11":
#         tryout_exercise11()
#     case "12":
#         tryout_exercise12()
#     case "13":
#         tryout_exercise13()
#     case "14":
#         tryout_exercise14()
#     case "15":
#         tryout_exercise15()
#     case "16":
#         tryout_exercise16()
#     case "17":
#         tryout_exercise17()
#     case "18":
#         tryout_exercise18()
#     case _:
#         print("we dont have this problem ready yet")

