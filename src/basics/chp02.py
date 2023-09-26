import math

print("chapter 2: For Loops")

# exercise 1
# for i in range (100): print("name for exerise1: counter = ",i+1)

# exercise 2
for i in range (50):
    for j in range(20):
        print("name",end="")
    print("")

# exercise 3
for i in range (100): print(i+1,"your name")

# exercise 4
for i in range (1,21): print(i,"----",round(math.pow(i,2)) )

# exercise 5
for i in range (8,90,3): print(i,",",sep="",end="" )
print("")

# exercise 6
for i in range (100,0,-2): print(i,",",sep="",end="" )
print("")

# exercise 7
# Write a program that uses exactly four for loops to print the sequence of letters below
# AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG

# exercise 8
name = input("enter your name")
counter = input("how many times you want to print it? ")
if not counter or not counter.isnumeric():
    print("\nyou did not enter numeric counter",counter)
else:
    for i in range(eval(counter)):
        print(name)

# exercise 9
# Program to display the Fibonacci sequence up to n-th term
nterms = input("How many terms? (numeric only)")

# first two terms
n1, n2 = 0, 1
count = 0

if not nterms or not nterms.isnumeric():
    print("\nyou did not enter numeric value", nterms)
else:
    # check if the number of terms is valid
    nterms = eval(nterms)
    if nterms <= 0:
       print("Please enter a positive integer")
    # if there is only one term, return n1
    elif nterms == 1:
       print("Fibonacci sequence upto",nterms,":")
       print(n1)
    # generate fibonacci sequence
    else:
       print("Fibonacci sequence:")
       while count < nterms:
           print(str(n1),",",sep="",end="")
           nth = n1 + n2
           # update values
           n1 = n2
           n2 = nth
           count += 1
       print("")


# exercise 10
wide = input("how much wide? (numeric): ")
high = input("how much high? (numeric): ")
if (not wide or not wide.isnumeric()) or (not high or not high.isnumeric()):
    print("one of the values was not numeric",wide,high)
else:
    wide = eval(wide)
    high = eval(high)
    print("---------------------")
    for i in range(high):
        print("*"*wide)
    print("---------------------")


# exercise 11
wide = input("how much wide? (numeric): ")
high = input("how much high? (numeric): ")
if (not wide or not wide.isnumeric()) or (not high or not high.isnumeric()):
    print("one of the values was not numeric",wide,high)
else:
    wide = eval(wide)
    high = eval(high)
    print("---------------------")
    for i in range(high):
        if i == 0 or i == high-1:
            print("*"*wide)
        else:
            print("*"," " * (wide - 2),"*",sep="")
    print("---------------------")

