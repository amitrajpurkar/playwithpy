from random import randint
from string import punctuation
from enum import Enum
from random import sample


# 1,2,5,8,17,18,22

def exercise01():
    """
    Write a program that asks the user to enter some text and then counts how many articles are
in the text. Articles are the words 'a', 'an', and 'the'.
    :return:
    """
    s = input("Enter some text: ")
    lst = s.split()
    articles = ["a","an","the"]
    # lst.count(articles)
    # print(f"there are {lst.count(articles)} articles in '{s}'")
    n = 0
    for w in lst:
        if w.lower() in articles:
            n += 1
    print(f"there are {n} articles in '{s}'")
    pass


# exercise01()


def exercise02():
    """
    Write a program that allows the user to enter five numbers (read as strings). Create a string
that consists of the user’s numbers separated by plus signs. For instance, if the user enters 2, 5, 11, 33, and 55, then the string should be '2+5+11+33+55'.
    """
    user_entry = input("Enter five numbers: ")
    conjunction = ["and", "or","&","|"]
    for c in punctuation:
        user_entry = user_entry.replace(c, "")
    for c2 in conjunction:
        user_entry = user_entry.replace(c2, " ")
    lst = user_entry.split()
    print("+".join(lst))
    pass


# exercise02()


def exercise05():
    """
    Write a simple quote-of-the-day program. The program should contain a list of quotes, and
when the user runs the program, a randomly selected quote should be printed.
    """
    quotes = [
        "The greatest glory in living lies not in never falling, but in rising every time we fall.",
        "The way to get started is to quit talking and begin doing.",
        "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.",
        "If life were predictable it would cease to be life, and be without flavor.",
        "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough."
    ]
    print(quotes[randint(0, len(quotes) - 1)])
    pass


class lottery(Enum):
    LOTTERY_NUM = [i for i in range(1,11)]

ITERATIONS = 1000

def lottery_hand():
    # Used sample function instead of calling the num of draws globally to practice with it.
    L = sample(lottery.LOTTERY_NUM.value, 6)
    return L

def winning_hand(ITERATIONS):
    count = 0
    for i in range(ITERATIONS):
        user_hand = lottery_hand()
        comp_hand = lottery_hand()
        if user_hand == comp_hand:
            count += 1
    return count

def exercise07():
    """
    Write a program that estimates the average number of drawings it takes before the user’s
numbers are picked in a lottery that consists of correctly picking six different numbers that
are between 1 and 10. To do this, run a loop 1000 times that randomly generates a set of
user numbers and simulates drawings until the user’s numbers are drawn. Find the average
number of drawings needed over the 1000 times the loop runs
    :return:
    """
    won = winning_hand(ITERATIONS)
    pc_won = won / ITERATIONS * 100
    # print((won / ITERATIONS) * 100)

    print(f"number of draws in 1000 cycles is {won} times")
    print(f"number of draws in 1000 cycles is {pc_won} %")
    pass


# exercise07()


def exercise08():
    """
    Write a program that simulates drawing names out of a hat. In this drawing, the number of
hat entries each person gets may vary. Allow the user to input a list of names and a list of
how many entries each person has in the drawing, and print out who wins the drawing.
    :return:
    """
    pass

# 17,18,22
from pprint import pprint
import numpy as np
from statistics import mean, median
def exercise17():
    """
    Write a program that finds the average of all of the entries in a 4 x 4 list of integers
    :return:
    """
    L = [[randint(1, 5) for _ in range(4)] for i in range(4)]
    # array = np.random.randint(5, size=(4, 4))
    # ave = array.mean()
    pprint(L)
    ave = mean([L[i][j] for i in range(len(L)) for j in range(len(L[0]))])
    print(f'The average of the matrix is {ave}.')
    pass


# exercise17()


def exercise18():
    """
Write a program that creates a 10 x 10 list of random integers between 1 and 100. Then do the
following:
(a) Print the list.
(b) Find the largest value in the third row.
(c) Find the smallest value in the sixth column
    :return:
    """
    n = 10
    L = [[randint(1, 100) for _ in range(n)] for i in range(n)]
    pprint(L)
    print("third row is",L[2])
    print("largest value in third row is",max(L[2]))
    print("sixth column is",[L[i][5] for i in range(len(L))])
    print("smallest value in sixth column is",min([L[i][5] for i in range(len(L))]))
    pass


# exercise18()


def exercise22():
    """
The following is useful as part of a program to play Battleship. Suppose you have a 5 x 5 list
that consists of zeroes and ones. Ask the user to enter a row and a column. If the entry in the
list at that row and column is a one, the program should print Hit and otherwise it should
print Miss.
    :return:
    """
    L = [[randint(0,1) for _ in range(5)] for i in range(5)]
    print("we have a 5 x 5 List of zeroes and ones.")
    r = int(input("enter a row (1 to 5): "))
    c = int(input("enter a column (1 to 5): "))
    if L[r-1][c-1] == 1:
        print("Hit")
    else:
        print("Miss")
    pprint(L)

    pass


exercise22()