# examples... 1-3,4,5, 8, 10, 14
import random


def exercise01():
    '''
    The code below prints the numbers from 1 to 50. Rewrite the code using a while loop to
    accomplish the same thing.
    for i in range(1,51):
    print(i)
    '''
    i = 1
    while i <= 50:
        print(i)
        i += 1
    pass


def exercise02():
    '''
    (a) Write a program that uses a while loop (not a for loop) to read through a string and print
    the characters of the string one-by-one on separate lines.
    (b) Modify the program above to print out every second character of the string
    '''
    s = input("Enter a string: ")
    print(" print the characters of the string one-by-one on separate lines.")
    i = 0
    while i < len(s):
        print(s[i])
        i += 1

    print("print every second character of the string")
    i = 0
    while i < len(s):
        print(s[i])
        i += 2
    pass


def exercise03():
    '''
    A good program will make sure that the data its users enter is valid. Write a program that
    asks the user for a weight and converts it from kilograms to pounds. Whenever the user
    enters a weight below 0, the program should tell them that their entry is invalid and then ask
    them again to enter a weight. [Hint: Use a while loop, not an if statement].
    :return:
    '''
    weight = float(input("Enter weight in kilograms: "))
    while weight < 0:
        print("invalid entry")
        weight = float(input("Enter weight in kilograms: "))
    print("the weight in pounds is ", weight * 2.2)
    pass


def exercise04():
    '''
    Write a program that asks the user to enter a password. If the user enters the right password,
    the program should tell them they are logged in to the system. Otherwise, the program
    should ask them to reenter the password. The user should only get five tries to enter the
    password, after which point the program should tell them that they are kicked off of the
    system.
    :return:
    '''
    stored_password = "itsme"
    password = input("Enter password: ")
    tries = 0
    while password != stored_password:
        password = input("Enter password: ")
        tries += 1
        if tries == 5:
            print("You are kicked off of the system")
            break
    pass


def exercise05():
    '''
    Write a program that allows the user to enter any number of test scores. The user indicates
    they are done by entering in a negative number. Print how many of the scores are A’s (90 or
    above). Also print out the average
    :return:
    '''
    a_score = 0
    total_score = 0
    number_of_scores = 0
    how_many_scores = eval(input("how many scores do you want to enter? "))
    while True:
        score = eval(input("Enter score: "))
        if score < 0:
            break
        if score >= 90:
            a_score += 1
        total_score += score
        number_of_scores += 1
        if number_of_scores == how_many_scores:
            break
    print("Number of A's = ", a_score)
    print("Average score = ", total_score / number_of_scores)
    pass


def exercise06():
    print("not ready yet")
    pass


def exercise07():
    print("not ready yet")
    pass


def exercise08():
    '''
    The GCD (greatest common divisor) of two numbers is the largest number that both are divisible
    by. For instance, gcd(18, 42) is 6 because the largest number that both 18 and 42 are
    divisible by is 6. Write a program that asks the user for two numbers and computes their gcd.
    Shown below is a way to compute the GCD, called Euclid’s Algorithm.
    • First compute the remainder of dividing the larger number by the smaller number
    • Next, replace the larger number with the smaller number and the smaller number with
    the remainder.
    • Repeat this process until the smaller number is 0. The GCD is the last value of the larger
    number.
    :return:
    '''
    first_number = eval(input("Enter first number: "))
    second_number = eval(input("Enter second number: "))
    small_number = min(first_number, second_number)
    large_number = max(first_number, second_number)
    while small_number != 0:
        remainder = large_number % small_number
        large_number = small_number
        small_number = remainder
    print("GCD = ", large_number)
    pass


def exercise09():
    print("not ready yet")
    pass


def exercise10():
    '''
    Write a program that has a list of ten words, some of which have repeated letters and some
    which don’t. Write a program that picks a random word from the list that does not have any
    repeated letters
    :return:
    '''
    L = ["apple", "banana", "strawberry", "kiwi",
         "pear", "melon", "orange", "grapes", "mango", "peach"]

    while True:
        selected_word = random.choice(L)
        print(selected_word)
        for c in selected_word:
            if selected_word.count(c) > 1:
                print("there are repeated letters in",selected_word)
                break
        else:
            print("there are no repeated letters in",selected_word)
            break
    pass


def exercise14():
    '''
    Write a program to play the following simple game. The player starts with $100. On each
    turn a coin is flipped and the player has to guess heads or tails. The player wins $9 for each
    correct guess and loses $10 for each incorrect guess. The game ends either when the player
    runs out of money or gets to $200
    :return:
    '''
    L = ["heads", "tails"]
    money = 100
    while 0 < money < 200:
        guess = input("Guess heads or tails (enter 'heads' or 'tails'): ")
        coin = random.choice(L)
        if guess == coin:
            money += 9
            print("You win $9, balance is now $", money)
        else:
            money -= 10
            print("You lose $10, balance is now $", money)
    print("You ended with $", money)
    if money >= 200:
        print("You win the game")
    elif money <= 0:
        print("You lose the game")
    pass


# exercise01()
# exercise02()
# exercise03()
# exercise04()
# exercise05()
# exercise06()
# exercise07()
# exercise08()
# exercise09()
# exercise10()
exercise14()
