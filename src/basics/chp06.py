

def try_exercise01():
    """
    Write a program that asks the user to enter a string. The program should then print the
    following:
    (a) The total number of characters in the string
    (b) The string repeated 10 times
    (c) The first character of the string (remember that string indices start at 0)
    (d) The first three characters of the string
    (e) The last three characters of the string
    (f) The string backwards
    (g) The seventh character of the string if the string is long enough and a message otherwise
    (h) The string with its first and last characters removed
    (i) The string in all caps
    (j) The string with every a replaced with an e
    (k) The string with every letter replaced by a space
    """
    s = input("Enter a string: a name, phrase, etc: ")
    while not s:
        s = input("Invalid; try again; Enter a string: ")
        continue
    print(f"total number of characters in {s} =", len(s))
    print("repeat 10 times... =",s*10)
    print(f"first character of {s} is =", s[0])
    print(f"first three characters of {s} are =", s[:3])
    print(f"last three characters of {s} are =", s[-3:])
    print(f"the string {s} backwards =", s[::-1])
    if len(s) >= 7:
        print(f"seventh character of {s} is =",s[7-1])
    else:
        print(f"the string {s} is not long enough")
    print(f"the string {s} with 1st, last char removed =",s[1:len(s)-1:1])
    print(f"the string {s} in all caps =",s.upper())
    print(f"in string {s}, replace every 'a' with 'e' =",s.replace("a","e"))
    print(f"in string {s}, replace every letter with space =", "|"+ " "*len(s) +"|")

    pass

# try_exercise01()

def try_exercise02():
    """
    A simple way to estimate the number of words in a string is to count the number of spaces
    in the string. Write a program that asks the user for a string and returns an estimate of how
    many words are in the string
    """
    s = input("Enter a phrase or a few words: ")
    lst = s.split()
    n = len(lst)
    print(f"Estimated {n} words in '{s}'")
    pass


def try_exercise03():
    """
    People often forget closing parentheses when entering formulas. Write a program that asks
    the user to enter a formula and prints out whether the formula has the same number of opening
    and closing parentheses
    :return:
    """
    s = input("Enter a maths/ algebra formula: ")
    opening_braces = s.count("(")
    closing_braces = s.count(")")
    if opening_braces == closing_braces:
        print(f"the opening and closing braces matched in '{s}'")
    else:
        print(f"opening / closing braces did not match in '{s}'")
    pass


try_exercise03()


def try_exercise04():
    pass


def try_exercise05():
    pass


def try_exercise06():
    pass


def try_exercise07():
    pass


def try_exercise08():
    pass


def try_exercise09():
    pass


def try_exercise10():
    pass


def try_exercise11():
    pass


def try_exercise12():
    pass


def try_exercise13():
    pass


def try_exercise14():
    pass


def try_exercise15():
    pass


def try_exercise16():
    pass


def try_exercise17():
    pass


def try_exercise18():
    pass


def try_exercise19():
    pass


def try_exercise20():
    pass


def try_exercise21():
    pass


def try_exercise22():
    pass


def try_exercise23():
    pass


def try_exercise24():
    pass


def try_exercise25():
    pass

