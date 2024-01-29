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


exercise01()


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


exercise02()


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


exercise03()


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


exercise04()


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