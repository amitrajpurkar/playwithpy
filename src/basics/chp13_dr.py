#EXERCISE 1
def rectangle(m,n):
    '''
    Write a function called rectangle that takes two integers m and n as arguments and prints
out an m * n box consisting of asterisks.
    :param m:
    :param n:
    :return:
    '''
    for i in range(m):
        print('*' * n)
    pass

# rectangle(2,4)


#EXERCISE 3
def sum_digits():
    '''
Write a function called sum_digits that is given an integer num and returns the sum of the
digits of num
    :return:
    '''
    i = 0
    num = input("Enter a number: ")
    if not num.isnumeric():
        num = input("that was not numeric, enter a number more than 2 digits: ")
    sum = 0
    for c in num:
        sum += eval(c)
    print("the sum of digits =",sum)
    pass

# sum_digits()


#EXERCISE 5
def first_diff(string1: str, string2: str) -> int:
    '''
    Write a function called first_diff that is given two strings and returns the first location in
which the strings differ. If the strings are identical, it should return -1
    :param string1:
    :param string2:
    :return:
    '''
    location_of_first_diff = 0
    if string1 == string2:
        location_of_first_diff = -1
        return location_of_first_diff

    short_word_length = min(len(string1), len(string2))
    for i in range(short_word_length):
        # print("characters are ",string1[i],string2[i])
        if string1[i] == string2[2]:
            continue
        elif string1[i] != string2[i]:
            location_of_first_diff = i + 1
            break
        else:
            # all characters till min-length are identical in both strings
            location_of_first_diff = short_word_length + 1
    # print("location number is ",location_of_first_diff)
    return location_of_first_diff
    pass

# string1 = input("Enter a string: ")
# string2 = input("Enter another string: ")
# print("The number at which there is a difference of values is, ", first_diff(string1, string2))


#EXERCISE 8
def number_of_factors():
    '''
    Write a function called number_of_factors that takes an integer and returns how many
factors the number has
    :return:
    '''
    number = int(input("Enter a number: "))
    factors = []
    for i in range(1, number+1):
        if (number%i) == 0:
            factors.append(i)
    print(*factors, sep=", ")
    pass

# number_of_factors()


#EXERCISE 13
def change_case():
    '''
    Write a function called change_case that given a string, returns a string with each upper
case letter replaced by a lower case letter and vice-versa
    :return:
    '''
    value = input("Enter a word: ")
    NewValue = value.swapcase()
    print(NewValue)
    pass

# change_case()