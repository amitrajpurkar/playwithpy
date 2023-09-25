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
    # sds


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
options['02. Give and hour and number of hrs, give what will the time in oclock'] = "exercise02"
options['03. Given a number, tell last x digits of that number'] = "exercise03"
options['04. Given weight in kgs, give the weight in pounds'] = "exercise04"
options['05. Given a number, tell the factorial of that'] = "exercise05"
options['06. Given a number, tell the sin, cos, tan of that number'] = "exercise06"
options['07. Given an angle in degrees, tell sine of that angle'] = "exercise07"
options['08. Tell sin, cos of angles from 0 to 345, increments of 15'] = "exercise08"
options['09. Given an year, find the date of Easter in that year'] = "exercise09"
options['10. Given an year, tell if its a Leap year or not'] = "exercise10"
options['11. Given an amount, tell how many quaters, dimes, nickels and pennies'] = "exercise11"
options['12. Given height and width, print a modular rectangle'] = "exercise12"
options['13. Given height and width, print a modular rectangle'] = "exercise13"
options['eg1. Guess a random number'] = "example01"


# Let user select an exercise
option = selectFromDict(options, 'option')
