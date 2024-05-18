#
#
#
#
#
#EXERCISE 1
def rectangle(m,n):
    for i in range(m):
        print('*' * n)
rectangle(2,4)

#EXERCISE 3
def sum_digits():
    i = 0
    num = input("Enter a number: ")
    if not num.isnumeric():
        num = input("that was not numeric, enter a number more than 2 digits: ")
    sum = 0
    for c in num:
        sum += eval(c)
    print("the sum of digits =",sum)
sum_digits()

#EXERCISE 5 ---------------VVVVV------------- NOT WORKING!!!!!! :(  ----------VVVVV---------------------------------------
def first_diff(string1, string2):
    
    #i = 0
    #while string1 != string2:
    #    for i in string1 and string2:
    #        i += 1
    min_length = min(len(string1), len(string2))
    for i in range(min_length):
        if string1[i] != string2[i]:
            return i
    if string1[i] == string2[2]:
        return -1
    else:
        return min_length
string1 = input("Enter a string: ")
string2 = input("Enter another string: ")

print("The number at which there is a difference of values is, ", first_diff(string1, string2))
#---------------------------------------------ABOVE WAS NOT WORKING------------------------------------------------------------
#EXERCISE 8
def number_of_factors():
    number = int(input("Enter a number: "))
    for i in range(1, number+1):
        if (number%i) == 0:
            print(i, end=' ')

number_of_factors()

#EXERCISE 13
def change_case():
    value = input("Enter a word: ")
    NewValue = value.swapcase()
    print(NewValue)
change_case()