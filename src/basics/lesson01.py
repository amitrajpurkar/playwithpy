# learning about commands in python
# In the Python programming language, commands basically refer to different functions or methods that we can execute on the python shell to work them as commands.

# https://www.interviewbit.com/blog/python-commands/#:~:text=In%20the%20Python%20programming%20language,to%20work%20them%20as%20commands.

# Know the definition of the commands
# Valid or Invalid variable names
# Math operators
# Tell output of print statements
# Write code using print, input and assignment statements

print("printing a text")
someVariable = 'constant string value'
print(someVariable)
print(someVariable.capitalize())
print(someVariable.upper())

num=7
print((num * 1),(num * 2),(num * 3),(num * 4),(num * 5),sep="---")

print("first val", "second val" , "third val", sep="---")


# lets now see the arithmetic operators
x = 7
y = 9
print(x * y) # gives 63
print(x + y) # gives 16
print(x - y) # gives -2
print(x / y) # gives 0.7777777777777778
print(y % x) # gives 2
print(y ** 2) # gives 81
print("-----")

print(y / x) # gives 1.2857142857142858
print(y // x) # gives 1
print(x // y) # gives 0
print(round(y / x, 3)) # gives 1.286
