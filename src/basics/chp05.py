from math import log
from random import randint

def try_exercise01():
    print("Write a program that counts how many of the squares \
     of the numbers from 1 to 100 end in a 1.")
    counter = 0
    squares_found = []
    for i in range(1, 101):
        sq = i ** 2
        if sq % 10 == 1:
            counter = counter + 1
            squares_found.append(sq)
    print("number of squares ending in 1 are", counter)
    print("those squares are", *squares_found, sep=",")
    pass


def try_exercise02():
    print("how many of the squares of the numbers from 1 to 100 end in a 4 or 9.")
    counter = 0
    squares_found = []
    for i in range(1, 101):
        sq = i ** 2
        if (sq % 10 == 4) or (sq % 10 == 9):
            counter = counter + 1
            squares_found.append(sq)
    print("number of squares ending in 4 or 9 are", counter)
    print("those squares are", *squares_found, sep=",")
    pass


def try_exercise03():
    num = input("enter a number: ")
    n = eval(num) if num.isnumeric() else 0
    accum = 0
    if n == 0:
        print("did you enter a number?",num)
        return None

    for i in range(1, n+1):
        accum = accum + 1/i
    accum = accum - log(n)
    print("the calc for (1+ 1/2+ 1/3+.. + 1/n) - log(n) is",accum)
    pass


def try_exercise04():
    pass


def try_exercise05():
    n = input("give a number: ")
    n = eval(n) if n.isnumeric() else 0
    divisors = []
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            divisors.append(i)
    # the number itself is also a divisor
    divisors.append(n)
    print("divisors of", n, "are", *divisors)
    print("sum of all divisors is", sum(divisors))
    pass


def try_exercise06():
    pass


def try_exercise07():
    pass


def try_exercise08():
    pass


def select_from_dict(choices, name):
    index = 0
    index_valid_list = []
    print('Which problem do you want to try: ')
    for optionName in choices:
        index = index + 1
        index_valid_list.extend([choices[optionName]])
        print(str(index) + ') ' + optionName)
    input_valid = False
    while not input_valid:
        input_raw = input(name + ': ')
        input_no = int(input_raw) - 1
        if input_no > -1 and input_no < len(index_valid_list):
            selected = index_valid_list[input_no]
            print('Selected ' +  name + ': ' + str(selected))
            if "exercise01" == selected:
                try_exercise01()
            elif "exercise02" == selected:
                try_exercise02()
            # elif "exercise03" == selected:
            #     try_exercise03()
            # elif "exercise04" == selected:
            #     try_exercise04()
            elif "exercise05" == selected:
                try_exercise05()
            # elif "exercise06" == selected:
            #     try_exercise06()
            # elif "exercise07" == selected:
            #     try_exercise07()
            # elif "exercise08" == selected:
            #     try_exercise08()
            # elif "exercise09" == selected:
            #     try_exercise09()
            # elif "exercise10" == selected:
            #     try_exercise10()
            # elif "exercise11" == selected:
            #     try_exercise11()
            # elif "exercise12" == selected:
            #     try_exercise12()
            # elif "exercise13" == selected:
            #     try_exercise13()
            else:
                print("we dont have this problem ready yet")

            # here call appropriate exercise-function
            retry = input("want to retry any problems? y/n: ").lower()
            if "y" == retry:
                input_valid = False
            else:
                input_valid = True
                break
        else:
            print('Please select a valid ' + name + ' number')
    return selected


# define a dictionary of choices
# [USER OPTION] = PROGRAM RESULT
options = {'01. print how many squares of numbers between 1, 100 end in 1': "exercise01",
           '02. print how many squares end in 4 or 9': "exercise02",
           '03. Given num n calculate (1+ 1/2 + 1/3...+ 1/n) - log(n)': "exercise03",
           '04. compute the sum 1-2+3-4+....+1999-2000': "exercise04",
           '05. given a number, print sum of divisors': "exercise05",
           '06. print perfect numbers less than 10000': "exercise06",
           '07. given an integer, tell if its squarefree or not': "exercise07",
           '08. given x, y, z, swap values x->y, y->z, z->x': "exercise08",
           '09. how many int 1-1000 are not perfect squares, cubes or fifths': "exercise09",
           '10. given 10 test scores find five aspects': "exercise10",
           '11. given a number, tell its factorial using multiplicative technique': "exercise11",
           '12. guess number 5 times and tell scores': "exercise12", '13. improve multiplication game': "exercise13",
           '14. the monty hall problem': "example01"}


# Let user select an exercise
option = select_from_dict(options, 'option')
