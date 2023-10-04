from random import randint

# class Chapter04:

def guess_a_number():
    num = randint(1, 10)
    guess = eval(input('Enter your guess: '))

    if guess == num:
        print('You got it!')
    else:
        print('Sorry. The number is ', num)
    pass

def tryout_exercise01():
    length=input("enter length in centimeters: ")
    if not length or not length.isnumeric():
        print("you did not enter numeric value", length)
    elif eval(length) < 0:
        print("the length entered was negative !!", length)
    else:
        length = eval(length)
        len_in_inches = length * 2.54
        print("the length",length," cms is equal to ",len_in_inches,"inches")
    pass

def tryout_exercise02():
    temp = input("give a temperature value: ")
    unit = input("what is the unit: Celcius/ Farenheit (C or F): ")
    converted_temp = None
    if not temp or not temp.isnumeric() or not unit or not unit.isnumeric():
        print("one of the inputs is not correct: ",temp, unit)
    else:
        temp = eval(temp)
        if "c" == unit.lower().strip():
            converted_temp = round(((9 / 5) * temp) + 32,3)
            print("temperature in Farenheit = ",converted_temp)
        elif "f" == unit.lower().strip():
            converted_temp = round(5 / 9 * (temp - 32), 3)
            print("temperature in Celcius = ", converted_temp)
        else:
            print("unknown unit of temperature",unit)

def tryout_exercise03():
    temp = input("enter a temperature in Celcius: ")
    if not temp or not temp.isnumeric():
        print("the input is not correct: ",temp)
    else:
        temp = eval(temp)
        if temp < -273.15:
            print("the temperature is invalid because it is below absolute zero")
        elif temp == -275.15:
            print("the temperature is absolute zero")
        elif temp > -275.15 and temp < 0:
            print("the temperature is below freezing")
        elif temp == 0:
            print("the temperature is at freezing point")
        elif temp > 0 and temp < 100:
            print("the temperature is at normal range")
        elif temp == 100:
            print("the temperature is at boiling point")
        elif temp > 100:
            print("the temperature is above boiling point")

def tryout_exercise04():
    credits = input("how many credits have you taken? ")
    if not credits or not credits.isnumeric():
        print("credits given is not numeric", credits)
    else:
        lvl = get_student_level(int(credits))
        print("the student is a",lvl)
    pass


def get_student_level(credits:int) -> str:
    student_level:str = None
    if credits <= 23:
        student_level = "freshman" 
    elif credits > 23 and credits <= 53:
        student_level = "somophore"
    elif credits > 53 and credits <= 83:
        student_level = "junior"
    elif credits >= 84:
        student_level = "senior"
    return student_level
    

def tryout_exercise05():
    num = randint(1, 10)
    guess = input('Guess a number: ')
    if not guess or not guess.isnumeric():
        print("you did not enter a number !!",guess)
    else:
        guess = int(guess)
        if guess == num:
            print('You got it!')
        else:
            print('Sorry. The number is ', num)

def tryout_exercise06():
    num_of_items = input("how many items are you buying? (in numbers only) ")
    if not num_of_items or not num_of_items.isnumeric():
        print("enter numeric value",num_of_items)
    else:
        num_of_items = int(num_of_items)
        cost = cost_based_on_volume(num_of_items)
        print("total cost = $",cost)
    pass

def cost_based_on_volume(num_of_items:int) -> int:
    high_price:int = 12  # -- if buying less than 10 items
    medium_price:int = 10  # -- if buying between 10 to 99
    low_price:int = 7  # -- if buying 100 or more
    total_cost:int = None
    if num_of_items < 10:
        total_cost = round((high_price * num_of_items), 2)
    elif num_of_items >= 10 and num_of_items <= 99:
        total_cost = round((medium_price * num_of_items), 2)
    elif num_of_items >= 100:
        total_cost = round((low_price * num_of_items), 2)
    return total_cost

def tryout_exercise07():
    x, y = input("enter two numbers ").split()
    if not x or not x.isnumeric() or not y or not y.isnumeric():
        print("input is not numeric", x, y)
    else:
        if abs(x - y) <= 0.001:
            print("close")
        else:
            print("not close")
    pass

def tryout_exercise08():
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

def tryout_exercise09():
    n = input("give a number: ")
    n = eval(n)
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            # yield i
            print(i)
    # yield n
    print(n)
    pass

def tryout_exercise10():
    print("multiplication game program for kids")
    for q in range(1,11):
        num_1 = randint(1, 10)
        num_2 = randint(1, 10)
        print("Question:"+str(q), num_1, "X", num_2)
        solution = eval(input("Enter Solution: "))

        if (solution == num_1 * num_2):
            print("YaY you got it Right!!")
        else:
            print(solution, "Your Answer is Wrong")
    pass

def tryout_exercise11():
    hour = input("Enter hour: ")
    am_pm = eval(input("am (1) or pm (2)? "))
    hrs_ahead = input("How many hours ahead? ")

    if hour.isnumeric() and hrs_ahead.isnumeric():
        total_hrs = eval(hour) + eval(hrs_ahead)
        if total_hrs > 12:
            hrs_after12 = total_hrs % 12
            if am_pm == 1: print("New hour:", hrs_after12, "pm")
            elif am_pm == 2: print("New hour:", hrs_after12, "am")
            else: print("should not get here")
        else:
            if am_pm == 1: print("New hour:", total_hrs, "am")
            elif am_pm == 2: print("New hour:", total_hrs, "pm")
            else: print("should not get here")
    else:
        print("one of the inputs was not numeric", hour, hrs_ahead, am_pm)
    pass

def tryout_exercise12():
    print("A jar of Halloween candy contains an unknown amount of candy -- guess it")
    # num_of_candies = 0
    # left_after_div_by_5 = num_of_candies % 5
    # left_after_div_by_6 = num_of_candies % 6
    # left_after_div_by_7 = num_of_candies % 7
    #5x + 2 = 6y + 3 = 7z + 2

    # for candies in range(200):
    #     if (candies % 5 != 2):
    #         continue
    #     if (candies % 6 != 3):
    #         continue
    #     if (candies % 7 != 2):
    #         continue
    #
    #     print(str(candies) + " candies are in the bowl!")
    #     break

    for i in range(200):
        if i % 5 == 2:
            if i % 6 == 3:
                if i % 7 == 2:
                    print(i, 'candies are in the bowl!')

    pass

def tryout_exercise13():
    print("program that lets the user play Rock-Paper-Scissors against the computer")
    rock = 1
    paper = 2
    scissor = 3
    # paper > rock > scissor > paper

    user_wins = 0
    computer_wins = 0
    draws = 0
    for i in range(5):
        compPick = randint(1,3) ## 1=rock; 2=paper; 3=scissor
        uPick = input("enter your number: 1.rock, 2.paper, 3.scissor: ")
        userPick = eval(uPick) if uPick.isnumeric() else 0
        if compPick == rock:
            if userPick == rock:
                draws = draws + 1
            elif userPick == paper:
                user_wins = user_wins + 1
            elif userPick == scissor:
                computer_wins = computer_wins + 1
        elif compPick == paper:
            if userPick == rock:
                computer_wins = computer_wins + 1
            elif userPick == paper:
                draws = draws + 1
            elif userPick == scissor:
                user_wins = user_wins + 1
        elif compPick == scissor:
            if userPick == rock:
                user_wins = user_wins + 1
            elif userPick == paper:
                computer_wins = computer_wins + 1
            elif userPick == scissor:
                draws = draws + 1
    print("Results -- user wins",user_wins,"times, computer wins",computer_wins,"times, and draws",draws,"times")
    pass


def selectFromDict(options, name):
    index = 0
    indexValidList = []
    print('Which problem do you want to try: ')
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
            if "exercise01" == selected:
                tryout_exercise01()
            elif "exercise02" == selected:
                tryout_exercise02()
            elif "exercise03" == selected:
                tryout_exercise03()
            elif "exercise04" == selected:
                tryout_exercise04()
            elif "exercise05" == selected:
                tryout_exercise05()
            elif "exercise06" == selected:
                tryout_exercise06()
            elif "exercise07" == selected:
                tryout_exercise07()
            elif "exercise08" == selected:
                tryout_exercise08()
            elif "exercise09" == selected:
                tryout_exercise09()
            elif "exercise10" == selected:
                tryout_exercise10()
            elif "exercise11" == selected:
                tryout_exercise11()
            elif "exercise12" == selected:
                tryout_exercise12()
            elif "exercise13" == selected:
                tryout_exercise13()
            elif "example01" == selected:
                guess_a_number()
            else:
                print("we dont have this problem ready yet")

            # here call appropriate exercise-function
            retry = input("want to retry this or other problems? y/n: ").lower()
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
options['01. Given length in cms, give length in inches'] = "exercise01"
options['02. given a temperature and unit, convert into other unit'] = "exercise02"
options['03. Given a temp in celcius, tel what range it is in'] = "exercise03"
options['04. Given credits, tell which grade the student is in'] = "exercise04"
options['05. Guess a number between 1 to 10'] = "exercise05"
options['06. Given number of items, tell the total cost'] = "exercise06"
options['07. given two numbers, tell if they are close or not'] = "exercise07"
options['08. Given an year, tell if its a Leap year or not'] = "exercise08"
options['09. Given a number, tell all its divisors'] = "exercise09"
options['10. ask 10 multiplications, check if answered right or wrong'] = "exercise10"
options['11. print how many hours in future'] = "exercise11"
options['12. guess candies in a bowl'] = "exercise12"
options['13. rock paper scisors 5 rounds'] = "exercise13"
options['eg1. Guess a random number'] = "example01"


# Let user select an exercise
option = selectFromDict(options, 'option')
