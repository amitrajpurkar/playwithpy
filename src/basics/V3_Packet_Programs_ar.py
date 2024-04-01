import re
import os

# ------------ section one functions ----------------

def print_shifting_text():
    """
    write a program to print a phrase "1989 COMPUTER CONTEST" on each line of the screen
    such that each line is indented by one extra space; NOTE: if you are using a 40-column display,
    the output may wrap on the screen
    :return:
    #1.1 - 10 points
    """
    s = "1989 COMPUTER CONTEST"
    s_len = len(s)
    for i in range(30):
        if i + s_len <= 40:
            print(" "*i, "1989 COMPUTER CONTEST")
        else:
            s_total = " "*i + s
            s_1st = s_total[0:39]
            s_2nd = s_total[39:]
            print(s_1st)
            print(s_2nd)
    pass


def storage_conversion():
    """
    a database is a collection of storage or information. databases often require much
    storage space. many businesses measure their databases in terms of gigabytes of data.
    a gigabyte is equivalent to 1024 or 2^10 megabytes. a megabytes is approximately
    a million bytes. write a program to represent a giga byte value in its
    equivalent number of megabytes. input will consist of a positive integer less than 30
    :return:
    #1.2 - 10 points
    """
    gb = eval(input("Enter number of gigabytes (give a number less than 30): "))
    mb = gb * 1024
    print(mb, "MEGABYTES")
    pass


def print_word_in_L_Shape():
    """
    write a program to print a word in a L shape
    :return:
    #1.3 - 10 points
    """
    aword = input("Enter a word: ")
    x = len(aword)-1
    for i in range(len(aword)):
        print(' '*x, aword[i], sep = '')
    print(aword)
    pass


def produce_pattern_A():
    """
    write a program to produce the following pattern (like an A) for an input integer, N. N should be between 1 and 9.
    :return:
    """
    n = eval(input("Enter a number between 1 and 9: "))
    space_cnt = n
    for i in range(1, n+1):
        if i ==1:
            print(" "*(space_cnt-i), i)
        else:
            print(" "*(space_cnt-i), i, " "*(i-1), i)
    pass


def correct_modern_date_for_christ():
    """
    Anno Domini is Latin for "in the year of our Lord" and is abbreviated as A.D.
    The abbreviation B.C. stands for "Before Christ". In 532 AD a monk, Dionysius Exiguus
    began a christian system of dating events, starting with the year, he believed Christ was born.
    The years before the birth are termed as BC while teh years after birth of christ are termed AD.
    Following is the order of years: 2 BC, 1 BC, 0 AD, 1 AD, 2 AD, 3 AD, 4 AD, etc. with
    Christ's birth being in the year 0 AD. today we know that the monk was in error.
    Even though we continue to use this dating system, biblical scholars currently believe that
    Christ was born four years earlier than what the monk had thought.

    write a program that corrects modern date to account for this change.
    :return:
    """
    year = eval(input("Enter a year: "))
    ad_bc = input("Enter A.D. or B.C.: ")
    print(year-4, ad_bc)
    pass


def password_checker():
    """
    many computer systems require a user to enter a password to ensure that the appropriate person
    is accessing his/ her files or information. write a program to prompt a user for a password
    with the words "ENTER PASSWORD:". For this program the users password is "ITSME". The user has
    upto three chances to enter the correct password. If it is corect, display the message "YOU HAVE ACCESS".
    For the first two tries if incorrect password is entered, display "INVALID PASSWORD" and prompt
    for another password.. After three incorrect tries display message, "YOU ARE TRESPASSING" and exit.
    :return:
    """
    pwd = "ITSME"
    attempt1 = input("ENTER PASSWORD: ")
    if attempt1 == pwd:
        print("YOU HAVE ACCESS")
    elif attempt1 != pwd:
        print("INVALID PASSWORD")
        attempt2 = input("ENTER PASSWORD: ")
        if attempt2 == pwd:
            print("YOU HAVE ACCESS")
        elif attempt2 != pwd:
            print("INVALID PASSWORD")
            attempt3 = input("ENTER PASSWORD: ")
            if attempt3 == pwd:
                print("YOU HAVE ACCESS")
            elif attempt3 != pwd:
                print("YOU ARE TRESPASSING")
    pass


def determine_best_dbms():
    """
    write a program to determine the best Database Management System, DBMS to use. a DBMS is a set of programs
    that access a set of inter-related data called database. A DBMS is good if it provides an environment
    that is both convenient and efficient to use in retrieving data from a database and in storing data into the database.

    First N will be input as the number of DBMS to be considered. next N names pertaining to those databases will be input.
    Each followed by its respective convenience rank and efficiency rank. (both between 1 and 10 inclusive).
    the best DBMS is determined by the total rank for convenience and efficiency.
    Display the name of the best DBMS followed by the words "IS BEST"
    :return:
    """
    n = eval(input("Enter number of DBMS: "))
    dbms_score = {}
    for i in range(n):
        name = input("Enter name of DBMS: ")
        conv, eff = input("Enter rank of convenience, efficiency: ").split(",")
        conv, eff = int(conv), int(eff)
        total = conv + eff
        dbms_score[name] = total
    best_score = max(dbms_score.values())
    for k, v in dbms_score.items():
        if v == best_score:
            print(k, "IS BEST")
    pass


def list_elem_no_repeat():
    """
    write a programs to display the elements fo a list, without repetitions, in the same order as they appear in the list.
    input will be one number at a time. termination of the list will be the input of the integer -999.
    :return:
    """
    lst = []
    while True:
        num = eval(input("Enter a number: "))
        if num == -999:
            break
        if num not in lst:
            lst.append(num)
    L_no_repeats = set(lst)
    print(*L_no_repeats, sep=" ")
    pass


def prob_to_feet_deep():
    """
    often statistician compute such large probabilities that they are difficult for an average person to comprehend.
    to help illustrate such a number, a real life model is used. write a program to illustrate
    the probability of 1 out of N, where N is a large real number, given in scientific E notation. Output
    will consist of the nearest integer of FEET DEEP of silver dollars with which the state of Texas
    needs to be covered to be equivalent to the number N. Output will be less than 1,000 and must be followed by FEET DEEP

    assume Texas has 262134 square miles area
    silver dollar diameter = 1.5 inches
    in2 = mi2 x 4,014,489,600
    :return:
    """
    pass


def logical_add_to_segment():
    """
    memory is a large array of bytes each with its won address. each program in the computer system
    deals with a particular logical address. the memory mapping hardware converts the logical
    address to physical addresses in the computer system. logical addresses are in the range of 0 to Max.
    the corresponding physical addresses are in the range of R+0 to R+Max, where the value R is the lower bound.

    write a program to mapa given logical address and segment to the corresponding physical address.
    each segment starts at a specific physical address (base) and has a given length. the physical address
    can be determined using the data in the table below by adding the base (smallest physical
    address in the specified segment) to the given logical address. if the logical address specified
    is greater than the length of the segment, display ADDRESSING ERROR. input will be the
    segment number followed by the logical address to convert. Output will be the error message or
    the physical address. repeat input until a segment number greater than 4 is entered.
    :return:
    """
    pass

# ------------ section two functions ----------------

def funct_2_1(i:int) -> int:
    if i <= 3:
        return round(1)
    else:
        return  round(((funct_2_1(i-1) * funct_2_1(i-2)) + 2) / funct_2_1(i-3))
    pass


def try_function_2_1():
    x = eval(input("Enter a positive integer x: "))
    print("Input x = ", x)
    print("F(x) = ", funct_2_1(x))
    pass


def function_2_1_dr():
    # x = eval(input("Enter a value of x, when all x values are greater than 3: "))
    # s = 1
    # r = 1
    # t = 1
    # a = x-1
    # b = x-2
    # c = x-3
    # if x == 1:
    #     print("F(", x, ") =", s)
    # elif x == 2:
    #     print("F(", x, ") =", r)
    # elif x == 3:
    #     print("F(", x, ") =", t)
    # elif x > 3 and x <= 10:
    #     if a == 1 or 2 or 3:
    #         a = s
    #         #y = (((s*b)+2)/c)
    #         #print("F(", x, ") =", y)
    #         if b == 1 or 2 or 3:
    #             b = r
    #             #y = (((a*r)+2)/c)
    #             #print("F(", x, ") =", y)
    #             if c == 1 or 2 or 3:
    #                 c = t
    #                 y = (((a*b)+2)/t)
    #                 print("F(", x, ") =", y)
    #     else:
    #         print("F(", x, ") =", y)
    #
    pass


def prime_factors_of_number():
    """
    write a program to print out the prime factorization equation for a given positive integer.
    The prime numbers must be in an increasing order and separated by X.
    :return:
    #2.1 - 20 points
    """
    n = eval(input("Enter a number: "))
    L = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            L.append(i)
            n //= i
        i += 1
    if n > 1:
        L.append(n)
    L.sort()
    print(*L, sep = " X ")
    pass


def word_without_vowels():
    """
    write a program to display a word without its vowels.
    :return:
    """
    s = input("Enter a word: ")
    vowels = "aeiouAEIOU"
    for i in s:
        if i in vowels:
            s = s.replace(i, "")
    print(s)
    pass


def name_to_abbr():
    """
    in order to write a program, a programmer should chooseappropriate names for variables, constants, procedures, etc.
    Each identifier should have a name that correctly identifies its purpose and function in the program.
    However if the name is too long, then it is burdensome to write and read in a program and may
    occupy more space on a line than is necessary. Good short names that properly describe an object's function
    are better than long names.

    for the sake of brevity, write a program to produce the shortest possible names for a set of
    six identifiers in a program so that each obe is distinguishable using the following method.
    if two or more identifiers start with same character(s) then compare each identifier
    character by character until they are distinguishable. truncate the remainder of the identifier
    after the distinguishable character. assume that the language can distinguish identifiers with any amount of letters if they differ.
    :return:
    """
    identifier1 = input("Enter an identifier 1: ")
    identifier2 = input("Enter an identifier 2: ")
    identifier3 = input("Enter an identifier 3: ")
    identifier4 = input("Enter an identifier 4: ")
    identifier5 = input("Enter an identifier 5: ")
    identifier6 = input("Enter an identifier 6: ")

    idntf = [identifier1, identifier2, identifier3, identifier4, identifier5, identifier6]
    abbr = []
    did_the_first_letters_match = False
    for i in idntf:
        remaining = idntf.remove(i)
        for idx in range(1, len(i)):
            for r in remaining:
                if i[:idx] not in r[:idx] :
                    did_the_first_letters_match = False
                else:
                    did_the_first_letters_match = True
                    break
            if did_the_first_letters_match == False:
                abbr.append(i[:idx])
    print(*abbr, ", ", sep="")

    pass


def factorial(n:int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def permutations_of_letters():
    """
    write a program to display the number of distinguishable permutations of letters of a given word.
    The mathematical formula for calculating such a number is given as the factorial, (!),
    of the number of letters in the word divided by ht eproduct of factorials of the number of times a letter appears.
    :return:
    """
    s = input("Enter a word: ")
    number_of_letters = len(s)
    counts_more_than_one = []
    characters_checked = []
    for c in s:
        if s.count(c) > 1 and c not in characters_checked:
            counts_more_than_one.append(s.count(c))
        characters_checked.append(c)
    print(counts_more_than_one)
    product_of_repeat_chars = 1
    for i in counts_more_than_one:
        product_of_repeat_chars *= factorial(i)

    print("OUTPUT: ", factorial(number_of_letters) / product_of_repeat_chars)
    pass


def underline_text():
    """
    write a program to simulate a word processor that underlines a text between two asterisks.
    underlining mode begins at first asterisk and ends at next asterisk.
    many different segments of the line can be underlined. the line of text will contain no more than 40 characters
    the program is to accept a line of text, clear teh screen, display the line, skip one line,
    display the line without the embedded asterisksm, then underline the text between the two consequtive asterisks
    :return:
    """
    s = input("Enter a line of text, with asterisks to show which part you want underlined: ")
    if len(s) > 40:
        print("Enter 40 or less letters, try again")
        return
    print(s)
    indexes = [i for i, c in enumerate(s) if c == "*"]
    if len(indexes) % 2 != 0:
        print("please enter an even number of asterisks, try again")
        return

    s_without_asterisks = s.replace("*", "")
    underline = re.sub("/w"," ",s[:indexes[0]])
    does_asterisk_start = True
    for i in range(len(indexes)-1):
        if does_asterisk_start:
            underline += re.sub("/w","-",s[indexes[i]:indexes[i+1]])
            does_asterisk_start = False
        else:
            underline += re.sub("/w"," ",s[indexes[i]:indexes[i+1]])
            does_asterisk_start = True

    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")
    print(s)
    print("/n")
    print(s_without_asterisks)
    print(underline)
    pass


def compute_int_expression():
    """
    write a program to compute an integer expression involving two positve integers
    separated by one of the following : +, -, *, /. each integer will contain no more than four digits.
    and the result is guaranteed to be an integer between -30,000 and 30,000.
    :return:
    """
    s = input("Enter an integer expression, with two numbers: ")
    print(s)
    nums = re.split(" + | - | * | / ", s)
    print("after split", nums)
    nums.remove("+") if "+" in s else nums
    nums.remove("-") if "-" in s else nums
    nums.remove("*") if "*" in s else nums
    nums.remove("/") if "/" in s else nums
    print("after removes", nums)
    if len(nums) != 2:
        print("please enter two numbers separated by +, -, *, or / ; try again")
    elif len(nums[0]) > 4 or len(nums[1]) > 4:
        print("please enter the numbers no more than four digits; try again")
    elif "+" in s:
        print("OUTPUT: ", int(nums[0]) + int(nums[1]))
    elif "-" in s:
        print("OUTPUT: ", int(nums[0]) - int(nums[1]))
    elif "*" in s:
        print("OUTPUT: ", int(nums[0]) * int(nums[1]))
    elif "/" in s:
        print("OUTPUT: ", int(nums[0]) / int(nums[1]))
    else:
        print("this condition is not possible")
    pass


def compute_int_expression2():
    s = input("Enter an integer expression, with two numbers: ")
    # print(s)
    nums = []
    nums = s.split("+") if "+" in s else nums
    nums = s.split("-") if "-" in s else nums
    nums = s.split("*") if "*" in s else nums
    nums = s.split("/") if "/" in s else nums
    # print("after split", nums)
    if len(nums) != 2:
        print("please enter two numbers separated by +, -, *, or / ; try again")
    elif len(nums[0]) > 4 or len(nums[1]) > 4:
        print("please enter the numbers no more than four digits; try again")
    elif "+" in s:
        print("OUTPUT: ", int(nums[0]) + int(nums[1]))
    elif "-" in s:
        print("OUTPUT: ", int(nums[0]) - int(nums[1]))
    elif "*" in s:
        print("OUTPUT: ", int(nums[0]) * int(nums[1]))
    elif "/" in s:
        print("OUTPUT: ", int(nums[0]) / int(nums[1]))
    else:
        print("this condition is not possible")
    pass

# ------------ section three functions ----------------



#
# #3.1 - 30 points
#
# #3.2 - 30 points
# pressure = eval(input("Enter value for P: "))
# #Thermo Equ: – 23511.9V + 988686.1 – (400943.0/V) = 9062.599P – 14.14PV^3


# ------------ invoke section ONE functions ----------------
# ------------ these give you 10 points --------------------
# print_shifting_text()       # 1.1
# storage_conversion()        # 1.2
# print_word_in_L_Shape()     # 1.3
# produce_pattern_A()         # 1.4 ... bug: the right arm not properly aligned
# correct_modern_date_for_christ() # 1.5
# password_checker()          # 1.6
# determine_best_dbms()       # 1.7
# list_elem_no_repeat()       # 1.8
# prob_to_feet_deep()         # 1.9
# logical_add_to_segment()    # 1.10

# ------------ invoke section TWO functions ----------------
# ------------ these give you 20 points --------------------
# try_function_2_1()          # 2.1
# prime_factors_of_number()   # 2.2...bug / solved
# word_without_vowels()       # 2.3
# name_to_abbr()              # 2.4.. bug + problem
# permutations_of_letters()   # 2.5... bug/ solved
# underline_text()            # 2.6
compute_int_expression2()    # 2.7.. bug/ solved


# ------------ invoke section THREE functions ----------------
# ------------ these give you 30 points --------------------
