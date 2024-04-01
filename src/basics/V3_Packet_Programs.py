#1.1 - 10 points
for i in range(20):
    print(" "*i, "1989 COMPUTER CONTEST")

#1.2 - 10 points
GB = eval(input("Enter number of gigabytes: "))
if GB > 30:
    pass
if GB <= 30:
    MB = GB * 1024
    print(MB, "MEGABYTES")
    
#1.3
aword = input("Enter a word: ")
x = len(aword)-1
for i in range(len(aword)):
    print(' '*x, aword[i], sep = '')
print(aword)

#1.6 - 10 points
password = "ITSME"
attempt1 = input("Enter Password: ")
if attempt1 == password:
    print("YOU HAVE ACCESS")
elif attempt1 != password:
    print("INVALID PASSWORD")
    attempt2 = input("Enter Password: ")
    if attempt2 == password:
        print("YOU HAVE ACCESS")
    elif attempt2 != password:
        print("INVALID PASSWORD")
        attempt3 = input("Enter Password: ")
        if attempt3 == password:
            print("YOU HAVE ACCESS")
        elif attempt3 != password:
            print("YOU ARE TRESPASSING")

#2.1 - 20 points
x = eval(input("Enter a value of x, when all x values are greater than 3: "))
s = 1
r = 1
t = 1
a = x-1
b = x-2
c = x-3
if x == 1:
    print("F(", x, ") =", s)
elif x == 2:
    print("F(", x, ") =", r)
elif x == 3:
    print("F(", x, ") =", t)
elif x > 3 and x <= 10:
    if a == 1 or 2 or 3:
        a = s
        #y = (((s*b)+2)/c)
        #print("F(", x, ") =", y)
        if b == 1 or 2 or 3:
            b = r
            #y = (((a*r)+2)/c)
            #print("F(", x, ") =", y)
            if c == 1 or 2 or 3:
                c = t
                y = (((a*b)+2)/t)
                print("F(", x, ") =", y)
    else:
        print("F(", x, ") =", y)

##2.2 - 20 points
#number = eval(input("Enter a number: "))


#2.3 - 20 points
word = input("Enter a word: ")
if word = 
print(word.replace("a", "e" "i" "o", "u"), "")

#3.1 - 30 points

#3.2 - 30 points
pressure = eval(input("Enter value for P: "))
#Thermo Equ: – 23511.9V + 988686.1 – (400943.0/V) = 9062.599P – 14.14PV^3