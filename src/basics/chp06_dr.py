#  UNIT 6 Notes
#
#   Basics, Concentration and Repetition, and in Operator
#     Input:x = len('Hello') -->   Output:5
#     Input:x = print('-'*75) -->   Output: *prints '-' 75 times*
#     Input: if '-' in string: -->   Output: *tells computer if the string contains '-'*
#     Input: if '-' not in string: -->   Output: *tells computer if the string does not contain '-'*
#                                                    
#                                                                       
#                                                                              
#   Indexing                                                                      
#                                                         
#     s='Python'
#                                                
#     Input: s[0]    -->   Output: P                                      
#     Input: s[1]    -->   Output: y                                  
#     Input: s[-1]   -->   Output: n                             
#     Input: s[-2]   -->   Output: o                                          
#     Input: s[3]    -->   Output: t                              
#                                                            
#                                                                      
#   Slices
#                                                                                                                           
#     index:   0 1 2 3 4 5 6 7 8 9                                                                      
#     letters: a b c d e f g h i j                                                                                 
#                                             
#     Input: s[2:5]   -->   Output: cde                                                                      
#     Input: s[ :5]   -->   Output: abcde                                                                                 
#     Input: s[5: ]   -->   Output: fghij                                                                                               
#     Input: s[-2: ]   -->   Output: ij                                                   
#     Input: s[ : ]   -->   Output: abcdefghij                                       
#     Input: s[1:7:2]   -->   Output: bdf                                                                      
#     Input: s[ : :-1]   -->   Output: jihgfedcba                                                                                 
#                                                                                                     
#
#
#  VVVVVV UNIT 6 EXERCISES VVVVVV

#     Exercise 1
exercise1 = input('Exercise 1 - Enter a string: ')
print('\t a. There are',len(exercise1), 'characters in the string')
print('\t b. The following is the string being repeated 10 times',exercise1*10,'.')
print('\t c. The first character of the string is',exercise1[0], '.')
print('\t d. The first three characters of the string is',exercise1[3], '.')
print('\t e. The last three characters of the string is',exercise1[-3], '.')
print('\t f. The following is the string displayed backwards',exercise1[ : :-1], '.')
if len(exercise1) >=7:
    print('\t g. The seventh character of your string is',exercise1[7], '.')
else:
    print('\t Too bad. Question "g" was skipped because your string is too small.')
print('\t h. The following is the string with its first and last characters removed',exercise1[1:len(exercise1)], '.')
print('\t i. The following is the string in all caps',exercise1.upper(), '.')
print('\t j. The following is the string with every "a" replaced with an "e"',exercise1.replace("a","e"), '.')


#     Exercise 2
string = input('Exercise 2 -- Enter a string: ')
space = string.count(' ')
if space == 0:
    print('There were no spaces, meaning you either put a word or nothing.')
elif space > 0:
    print('There are',space+1,'words.')


#     Exercise 3
query = input("Exercise 3 --- Enter a formula: ")
paranthesisOpen = string.count('(')
paranthesisClosed = string.count(')')
if paranthesisOpen == paranthesisClosed:
    print("YES! Your formula has the same number of open and closed paranthesis!")
elif paranthesisOpen != paranthesisClosed:
    print("Whoops! Your formula has an unequal amount of paranthesis. Check again.")


#     Exercise 4
word = input("Exercise 4 ---- Enter a word: ")
vowels = word.count('a' and 'e' or 'i' and 'o' or 'u')
if vowels == 0:
    print('Your word does not contain any vowels.')
elif vowels > 0:
    print("Your word does indeed contain vowels.")


#     Exercise 5
new_string = input('Exercise 5 ----- Enter a word: ')
new_string = new_string[:2]+'*'+new_string+'!!!'
print(new_string)


#     Exercise 6
s = input("Exercise 6 ------ Enter a string (word or phrase): ")
s = s.lower()
s = s.replace('.', '')
s = s.replace(',', '')
print(s)


#     Exercise 7
palindrome = input("Exercise 7 ------- Enter a palindrome: ")
palindrome_reverse = palindrome[ : :-1]
if palindrome == palindrome_reverse:
    print("Thou hath typed a palindrome!")
elif palindrome != palindrome_reverse:
    print("You didn't type a palindrome.. :( ")


#     Exercise 8
studentEMAILending = '@student.college.edu'
professorEMAILending = '@prof.college.edu'
EMAIL_Query = eval(input("How many email addresses will you be entering?  "))
if EMAIL_Query == 1:
    EMAIL_QUERY1 = input("Enter the email address: ")
    if studentEMAILending in EMAIL_QUERY1:
        print("You entered a student email.")
    elif professorEMAILending in EMAIL_QUERY1:
        print("You entered a Professor email.")
elif EMAIL_Query > 1:
    for i in range(EMAIL_Query):
        EMAIL_QUERY2 = input("Enter the email address: ")
        if studentEMAILending in EMAIL_QUERY2:
            print("You entered a student email.")
        elif professorEMAILending in EMAIL_QUERY2:
            print("You entered a Professor email.")


#      Exercise 12
wonkyword = input("Enter a word: ")
odd = (wonkyword.count())%2
if wonkyword is odd:
    for i in range(wonkyword.count()):
        
    
    
print()
#      Exercise 13
#      Exercise 14
#      Exercise 15
#      Exercise 18
#      Exercise 19