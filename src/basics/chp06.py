

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


# try_exercise03()


def try_exercise04():
    """
    Write a program that asks the user to enter a word and prints out whether that word contains
    any vowels -- a, e, i, o, u
    :return:
    """
    vowels = ["a","e","i","o","u"]
    s = input("Enter a word: ")
    n = 0
    for v in vowels:
        n += s.count(v) if s.find(v) != -1 else 0
    print(f"the given word {s} has {n} vowels.")
    pass


# try_exercise04()


def try_exercise05():
    """
    Write a program that asks the user to enter a string. The program should create a new string
    called new_string from the user’s string such that the second character is changed to an
    asterisk and three exclamation points are attached to the end of the string. Finally, print
    new_string
    :return:
    """
    s = input("Enter a string: ")
    new_s = s.replace(s[2-1],"*") + "!!!"
    print(f"transforming {s} into {new_s} ")
    pass


# try_exercise05()


def try_exercise06():
    """
    Write a program that asks the user to enter a string s and then converts s to lowercase, removes
    all the periods and commas from s, and prints the resulting string
    :return:
    """
    s = input("Enter a string: ")
    new_s = s.lower()
    new_s = new_s.replace(".","")
    new_s = new_s.replace(",","")
    print(f"transforming to {new_s}")
    pass


# try_exercise06()


def try_exercise07():
    """
    Write a program that asks the user to enter a word and determines whether the word is a
    palindrome or not. A palindrome is a word that reads the same backwards as forwards
    :return:
    """
    s = input("Enter a string: ")
    backward = s[::-1]
    if s == backward:
        print(f"the given word {s} is a Palindrome")
    else:
        print("the given word is not a Palindrome")
    pass


# try_exercise07()


def try_exercise08():
    """
    At a certain school, student email addresses end with @student.college.edu, while professor
    email addresses end with @prof.college.edu. Write a program that first asks the
    user how many email addresses they will be entering, and then has the user enter those addresses.
    After all the email addresses are entered, the program should print out a message
    indicating either that all the addresses are student addresses or that there were some professor
    addresses entered.
    :return:
    """
    student_address = "@student.college.edu"
    professor_address = "@prof.college.edu"
    n = input("How many email addresses you want to enter? ")
    while not n or not n.isnumeric():
        n = input("Invalid; enter the number of email addresses again: ")
        continue
    s = p = o = 0
    for i in range(eval(n)):
        email = input(f"email {i+1} = ")
        if email.endswith(student_address):
            s += 1
        elif email.endswith(professor_address):
            p += 1
        else:
            o += 1
    print(f"out of the email addresses entered, we have {s} students, {p} professors and {o} others")
    pass


# try_exercise08()


def try_exercise09():
    """
    Ask the user for a number and then print the following, where the pattern ends at the number
    that the user enters
    :return:
    """
    space = " "
    n = eval(input("Enter a number: "))
    for i in range(n):
        print((space * i) + str(i + 1))
    pass


# try_exercise09()


def try_exercise10():
    """
    Write a program that asks the user to enter a string, then prints out each letter of the string
    doubled and on a separate line.
    :return:
    """
    s = input("Enter a string: ")
    for c in s:
        print(c*2)
    pass


# try_exercise10()


def try_exercise11():
    """
    Write a program that asks the user to enter a word that contains the letter a. The program
    should then print the following two lines: On the first line should be the part of the string up
    to and including the first a, and on the second line should be the rest of the string
    :return:
    """
    s = input("Enter a word that contains letter a: ")
    idx = s.find("a")
    print("part of string till a = ",s[0:idx+1])
    print("part of string after a = ",s[idx+1:])
    pass


# try_exercise11()


def try_exercise12():
    """
    Write a program that asks the user to enter a word and then capitalizes every other letter of
    that word. So if the user enters rhinoceros, the program should print rHiNoCeRoS
    :return:
    """
    pass


# try_exercise12()


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

