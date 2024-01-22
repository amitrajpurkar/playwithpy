

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
    s = input("Enter a word: ")
    flag = True
    for c in s:
        if flag:
            print(c.upper(),end="")
            flag = False
        else:
            print(c,end="")
            flag = True
    pass


# try_exercise12()


def try_exercise13():
    """
    Write a program that asks the user to enter two strings of the same length. The program
    should then check to see if the strings are of the same length. If they are not, the program
    should print an appropriate message and exit. If they are of the same length, the program
    should alternate the characters of the two strings. For example, if the user enters abcde and
    ABCDE the program should print out AaBbCcDdEe
    :return:
    """
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    if s1.__len__() != s2.__len__():
        print("The two strings are not of the same length")
        return
    for i in range(s1.__len__()):
        print(s1[i],s2[i],sep="",end="")
    pass


# try_exercise13()


def try_exercise14():
    """
    Write a program that asks the user to enter their name in lowercase and then capitalizes the
    first letter of each word of their name.
    :return:
    """
    s = input("Enter your full name in lowercase: ")
    tokens = s.split()
    for token in tokens:
        print(token[0].upper(),end="")
        for c in token[1:]:
            print(c.lower(),end="")
        print(" ",end="")
    pass


# try_exercise14()


def try_exercise15():
    """
    When I was a kid, we used to play this game called Mad Libs. The way it worked was a friend
    would ask me for some words and then insert those words into a story at specific places
    and read the story. The story would often turn out to be pretty funny with the words I had
    given since I had no idea what the story was about. The words were usually from a specific
    category, like a place, an animal, etc.
    For this problem you will write a Mad Libs program. First, you should make up a story and
    leave out some words of the story. Your program should ask the user to enter some words
    and tell them what types of words to enter. Then print the full story along with the inserted
    words. Here is a small example, but you should use your own (longer) example:
    Enter a college class: CALCULUS
    Enter an adjective: HAPPY
    Enter an activity: PLAY BASKETBALL
    CALCULUS class was really HAPPY today. We learned how to
    PLAY BASKETBALL today in class. I can't wait for tomorrow's
    class!
    :return:
    """
    name = input(" What is your name: ")
    country = input("Where are you from: ")
    dream = input("What is your dream? ")
    user_story = "Dear {name}, you will be a good programmer one day. " \
                 "Always remember practice and practise till you make progress." \
                 "You are from {country}, which is a beautiful place. " \
                 "Believe in yourself, trust your instinct, " \
                 "always keep your sense of wonder alive. Keep exploring " \
                 "and keep trying till you achive your dream: {dream}".format(
        name=name, country=country, dream=dream)

    print(user_story)

    pass


# try_exercise15()


def try_exercise16():
    pass


def try_exercise17():
    pass


def try_exercise18():
    """
    The goal of this exercise is to see if you can mimic the behavior of the in operator and the
    count and index methods using only variables, for loops, and if statements.
    (a) Without using the in operator, write a program that asks the user for a string and a letter
    and prints out whether or not the letter appears in the string.
    (b) Without using the count method, write a program that asks the user for a string and a
    letter and counts how many occurrences there are of the letter in the string.
    (c) Without using the index method, write a program that asks the user for a string and
    a letter and prints out the index of the first occurrence of the letter in the string. If the
    letter is not in the string, the program should say so.
    :return:
    """
    s = input("Enter a string: ")
    l = input("Enter a letter: ")

    # part a
    for c in s:
        if c == l:
            print("the letter",l, "is in the string",s)
            break
    else:
        print("the letter",l, "is not in the string",s)

    # part b
    count = 0
    for c in s:
        if c == l:
            count += 1
    print("the letter",l, "appears",count,"times in the string",s)

    # part c
    index = -1
    isLetterFound = False
    for c in s:
        index += 1
        if c == l:
            isLetterFound = True
            print("the letter",l, "appears at index",index,"in the string",s)
            break
    if not isLetterFound:
        print("the letter",l, "is not in the string",s)

    pass


# try_exercise18()


def try_exercise19():
    """
    Write a program that asks the user for a large integer and inserts commas into it according
    to the standard American convention for commas in large numbers. For instance, if the user
    enters 1000000, the output should be 1,000,000
    :return:
    """
    n = input("Enter a large integer: ")
    n = int(n)
    print("{:,}".format(n))

    pass


# try_exercise19()


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

