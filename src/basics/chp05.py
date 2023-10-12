from math import log
from math import sqrt
from random import randint
from statistics import mean

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


def try_exercise09():
    count = 0
    for num in range(1, 1001):
        if sqrt(num) % 1 != 0 and (num ** (1 / 3)) % 1 != 0 and (num ** (1 / 5)) % 1 != 0:
            count += 1
    print(f'There are {count} numbers that are not perfect squares, cubes, or fifths.')
    pass


"""
Ask the user to enter 10 test scores. Write a program to do the following:
(a) Print out the highest and lowest scores.
(b) Print out the average of the scores.
(c) Print out the second largest score.
(d) If any of the scores is greater than 100, then after all the scores have been entered, print
a message warning the user that a value over 100 has been entered.
(e) Drop the two lowest scores and print out the average of the rest of them.
"""
def try_exercise10_1():
    mylist = []
    for i in range(10):
        score = eval(input(f'Enter Test Score {i + 1}: '))
        while score < 0 or score > 100:
            score = eval(input(f'Invalid. Enter Test Score {i + 1}: '))
            continue
        mylist.append(score)

    mylist.sort(reverse=True)
    max_score = max(mylist)
    min_score = min(mylist)
    max2_score = mylist[1]
    ave_score = mean(mylist)
    ave2_score = mean(mylist[:-2])

    print(f'The maximum score was {max_score} and the minimum score was {min_score}.')
    print(f'The 2nd largest score was {max2_score}.')
    print(f'The average was {ave_score}. The average score with the two lowaest scores dropped is {ave2_score}.')
    pass


def try_exercise10():
    first_score = eval(input('Enter Test Score 1: '))
    largest = first_score
    smallest = first_score
    large2 = first_score
    small2 = first_score
    total = first_score
    for i in range(9):
        score = eval(input(f'Enter Test Score {i + 2}: '))
        while score < 0 or score > 100:
            score = eval(input(f'Invalid. Enter Test Score {i + 2}: '))
            continue
        if score > largest:
            largest = score
        if score < smallest:
            smallest = score
        if largest > score > large2:
            large2 = score
        if small2 > score > smallest:
            small2 = score
        total += score

    max_score = largest
    min_score = smallest
    max2_score = large2
    ave_score = round(total / 10)
    ave2_score = round((total - smallest - small2) / 8)

    print(f'The maximum score was {max_score} and the minimum score was {min_score}.')
    print(f'The 2nd largest score was {max2_score}.')
    print(f'The average was {ave_score}. The average score with the two lowaest scores dropped is {ave2_score}.')
    pass

"""
Write a program that computes the factorial of a number. 
The factorial, n!, of a number n is the product of all the integers between 1 and n, 
including n. For instance, 5! = 1 x 2 x 3 x 4 x 5 = 120.
[Hint: Try using a multiplicative equivalent of the summing technique.]
"""
def try_exercise11():
    num = eval(input('Enter a number: '))
    fac = 1
    for i in range(1, num+1):
        fac *= i
    print(f'Factorial is {fac}.')
    pass


"""
Write a program that asks the user to guess a random number between 1 and 10. If they guess
right, they get 10 points added to their score, and they lose 1 point for an incorrect guess. Give
the user five numbers to guess and print their score after all the guessing is done
"""
def try_exercise12():
    score = 0
    for i in range(5):
        comp_guess = randint(1, 10)
        user_guess = eval(input('Enter guess between 1 and 10: '))
        while user_guess < 0 or user_guess > 10:
            user_guess = eval(input('Invalid. Enter guess between 1 and 10 again: '))
            continue
        if user_guess == comp_guess:
            score += 10
            print(f'You guessed right! Your score is {score}.')
        else:
            score -= 1
            print(f'Wrong. Computer guessed {comp_guess}. You guessed {user_guess}.')
    print(f'\nAfter 5 rounds, your total score is {score}.')
    pass


"""
In the last chapter there was an exercise that asked you to create a multiplication game for
kids. Improve your program from that exercise to keep track of the number of right and
wrong answers. At the end of the program, print a message that varies depending on how
many questions the player got right.
"""
def try_exercise13():
    print("multiplication game program for kids")
    rights = 0
    wrongs = 0
    for q in range(1, 11):
        num_1 = randint(1, 10)
        num_2 = randint(1, 10)
        print(f"Question {q}:  {num_1} X {num_2}= ?")
        solution = eval(input("Enter Solution: "))

        if solution == num_1 * num_2:
            rights += 1
            print("YaY you got it Right!!")
        else:
            wrongs += 1
            print(solution, "Your Answer is Wrong")
        print(f"in all you got {rights} right answers and {wrongs} wrong answers")
    pass


def try_exercise14():
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
            elif "exercise09" == selected:
                try_exercise09()
            elif "exercise10" == selected:
                try_exercise10()
            elif "exercise11" == selected:
                try_exercise11()
            elif "exercise12" == selected:
                try_exercise12()
            elif "exercise13" == selected:
                try_exercise13()
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
