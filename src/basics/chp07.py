from random import *

def exercise01():
    """
    Write a program that asks the user to enter a list of integers. Do the following:
    (a) Print the total number of items in the list.
    (b) Print the last item in the list.
    (c) Print the list in reverse order.
    (d) Print Yes if the list contains a 5 and No otherwise.
    (e) Print the number of fives in the list.
    (f) Remove the first and last items from the list, sort the remaining items, and print the
    result.
    (g) Print how many integers in the list are less than 5
    """
    L:list = eval(input("Enter a list of integers: "))

    print("total number of items in the list =", len(L))
    print("last item in the list =", L[-1])
    print("list in reverse order =", L[::-1])
    if 5 in L:
        print("Yes, the list contains a 5")
    else:
        print("No, the list does not contain a 5")
    print("number of fives in the list =", L.count(5))
    original_list = L.copy()
    L.remove(L[0])
    L.remove(L[-1])
    L.sort()
    print("result after removing 1st, last and then sort remaining =", L)
    print("how many integers in the list are less than 5 =",
          len([x for x in original_list if x < 5]))
    pass




def exercise02():
    """
Write a program that generates a list of 20 random numbers between 1 and 100.
(a) Print the list.
(b) Print the average of the elements in the list.
(c) Print the largest and smallest values in the list.
(d) Print the second largest and second smallest entries in the list
(e) Print how many even numbers are in the list.
    """
    L = [randint(1, 100) for i in range(20)]
    """
    L = []
    for i in range(20):
        L.append(randint(1,100))
    """
    print("list =", L)
    print("average of the elements in the list =", sum(L) / len(L))
    print("largest and smallest values in the list =", max(L), min(L))
    L.sort()
    print("second largest and second smallest entries in the list =", L[1], L[-2])
    print("how many even numbers are in the list =", len([x for x in L if x % 2 == 0]))

    pass


def exercise03():
    """
    Start with the list [8,9,10]. Do the following:
    (a) Set the second entry (index 1) to 17
    (b) Add 4, 5, and 6 to the end of the list
    (c) Remove the first entry from the list
    (d) Sort the list
    (e) Double the list
    (f) Insert 25 at index 3
    The final list should equal [4,5,6,25,10,17,4,5,6,10,17]
    :return:
    """
    L:list = [8,9,10]
    print("initial list =", L)
    L[1] = 17
    print("after setting second entry to 17 =", L)
    L.extend([4,5,6])
    print("after adding 4,5,6 to the end =", L)
    L.pop(0)
    print("after removing the first entry =", L)
    L.sort()
    print("after sorting =", L)
    L.extend(L)
    print("after doubling =", L)
    L.insert(3,25)
    print("the final outcome is:",L)
    pass


def exercise04():
    """
    Ask the user to enter a list containing numbers between 1 and 12.
    Then replace all of the entries in the list that are greater than 10 with 10.
    :return:
    """
    L:list = eval(input("Enter a list containing numbers between 1 and 12: "))
    print("original list :",L)
    L = [10 if x > 10 else x for x in L]
    print("after replacing numbers greater than 10 with 10 :",L)
    pass


def exercise05():
    """
    Ask the user to enter a list of strings. Create a new list that
    consists of those strings with their first characters removed
    :return:
    """
    L:list = eval(input("Enter a list of strings: "))
    print("original list :",L)
    L = [x[1:] for x in L]
    print("after removing the first character of each string :",L)
    pass


def exercise06():
    """
    Create the following lists using a for loop.
    (a) A list consisting of the integers 0 through 49
    (b) A list containing the squares of the integers 1 through 50.
    (c) The list ['a','bb','ccc','dddd', . . . ] that ends with 26 copies of the letter z.
    :return:
    """
    L1:list = [i for i in range(50)]
    # L1 =[]
    # for i in range(50):
    #     L1.append(i)
    print("list of integers 0 till 49 :",L1)
    L2:list = [(i+1)**2 for i in range(50)]
    print("list of squares of integers 1 till 50 :",L2)
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    L3:list = [alphabets[i] * (i+1) for i in range(26)]
    print("list of alphabets that starts with a, bb, ccc and ends with 26 copies of the letter z :",L3)
    pass


def exercise07():
    """
    Write a program that takes any two lists L and M of the same size and adds their elements
    together to form a new list N whose elements are sums of the corresponding elements in L
    and M. For instance, if L=[3,1,4] and M=[1,5,9], then N should equal [4,6,13].
    :return:
    """
    L:list = eval(input("Enter a list of Integers: "))
    M:list = eval(input("Enter second list of Integers: "))
    if len(L) != len(M):
        print("both lists need to be of same size")
    else:
        N:list = [L[i] + M[i] for i in range(len(L))]
        print("sum of the corresponding elements in L and M =", N)
    pass


def exercise08():
    """
    Write a program that asks the user for an integer and creates a list that consists of the factors
    of that integer`
    :return:
    """
    int_from_user = int(input("Enter an integer: "))
    L:list = [i for i in range(1,int_from_user+1) if int_from_user % i == 0]
    print(f"factors of the given Integer {int_from_user} are ",L)
    pass


def exercise09():
    """
    When playing games where you have to roll two dice, it is nice to know the odds of each
    roll. For instance, the odds of rolling a 12 are about 3%, and the odds of rolling a 7 are about
    17%. You can compute these mathematically, but if you don’t know the math, you can write
    a program to do it. To do this, your program should simulate rolling two dice about 10,000
    times and compute and print out the percentage of rolls that come out to be 2, 3, 4, . . . , 12.
    :return:
    """
    dice_roll = []
    outcome = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    sim = 10000
    for i in range(sim):
        dice_roll.append(randint(1, 6) + randint(1, 6))
    for i in dice_roll:
        outcome[i] += 1
    for key in outcome:
        outcome[key] = (outcome[key] / sim) * 100
        print("Odds of rolling a " + str(key) + " is " + str(outcome[key]) + "%")
    pass


def exercise10():
    """
    Write a program that rotates the elements of a list so that the element at the first index moves
    to the second index, the element in the second index moves to the third index, etc., and the
    element in the last index moves to the first index
    :return:
    """
    L:list = eval(input("Enter a list of Integers: "))
    print("original list :",L)
    L = L[1:] + L[:1]
    print("rotated list :",L)
    pass


def exercise11():
    """
    Using a for loop, create the list below, which consists of ones separated by increasingly many
    zeroes. The last two ones in the list should be separated by ten zeroes.
    [1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]
    :return:
    """
    L:list = []
    for i in range(10):
        L.append(1)
        for j in range(i):
            L.append(0)
    print("desired list = ",L)
    pass


def exercise12():
    """
    Write a program that generates 100 random integers that are either 0 or 1. Then find the
    longest run of zeros, the largest number of zeros in a row. For instance, the longest run of
    zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.
    :return:
    """
    L:list = []
    for i in range(100):
        L.append(randint(0,1))
    print("generated list = ",L)
    # print("longest run of zeros = ",L.count(0))

    count = 0
    max_count = 0
    for j in L:
        count = count + 1 if j == 0 else 0
        max_count = count if count > max_count else max_count
    print("longest run of zeros = ",max_count)
    pass


def exercise13():
    """
    Write a program that removes any repeated items from a list so that each item appears at most
    once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].
    :return:
    """
    L = [1,1,2,3,4,3,0,0]
    print("original list = ",L)
    # L = list(set(L))
    # print("unique list = ",L)

    new_L = []
    for i in L:
        if i not in new_L:
            new_L.append(i)
    print("unique list without duplicates = ",new_L)
    pass


def exercise14():
    """
    Write a program that asks the user to enter a length in feet. The program should then give
    the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
    meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
    enter a 2, then the program converts to yards, etc. While this can be done with if statements,
    it is much shorter with lists and it is also easier to add new conversions if you use lists
    :return:
    """
    given_length = int(input("Enter a length in feet: "))
    units = ["inches", "yards", "miles", "millimeters", "centimeters", "meters", "kilometers"]
    conversions = [12, 3, 1760, 304.8, 30.48, 0.3048, 0.0003048]
    print("1. inches \n2. yards \n3. miles \n4. millimeters \n5. centimeters \n6. meters \n7. kilometers")
    unit_chosen = int(input("Enter the unit you want to convert to: "))
    if unit_chosen >= 1 and unit_chosen <= 7:
        print(f"{given_length} feet in {units[unit_chosen-1]} = {given_length * conversions[unit_chosen-1]} {units[unit_chosen-1]}")
    else:
        print("Please enter a valid unit")
    pass


def exercise15():
    """
    There is a provably unbreakable cipher called a one-time pad. The way it works is you shift
    each character of the message by a random amount between 1 and 26 characters, wrapping
    around the alphabet if necessary. For instance, if the current character is y and the shift is 5,
    then the new character is d. Each character gets its own shift, so there needs to be as many
    random shifts as there are characters in the message. As an example, suppose the user enters
    secret. The program should generate a random shift between 1 and 26 for each character.
    Suppose the randomly generated shifts are 1, 3, 2, 10, 8, and 2. The encrypted message would
    be thebmv.
    (a) Write a program that asks the user for a message and encrypts the message using the
    one-time pad. First convert the string to lowercase. Any spaces and punctuation in the
    string should be left unchanged. For example, Secret!!! becomes thebmv!!! using
    the shifts above.
    (b) Write a program to decrypt a string encrypted as above.
    The reason it is called a one-time-pad is that the list of random shifts should only be used once.
    It becomes easily breakable if the same random shifts are used for more than one message.
    Moreover, it is only provably unbreakable if the random numbers are truly random, and the
    numbers generated by randint are not truly random. For this problem, just use randint,
    but for cryptographically safe random numbers, see Section 22.8
    :return:
    """
    s = input("Enter a message: ")
    s = s.lower()
    print(s)
    for c in s:
        print(chr(ord(c)+randint(1,26)),end="")
    pass



exercise01()
# exercise02()
# exercise03()
# exercise04()
# exercise05()
# exercise06()
# exercise07()
# exercise08()
# exercise09()
# exercise10()
# exercise11()
# exercise12()
# exercise13()
# exercise14()
# exercise15()