'''
Course: CIS 128 - Coumputer Programming 1
Assignment 3
Date: 05/10/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercise 1: The following program let the user input the year.
The program will check whether the year is a leap year or not.

print ("Please input the year ", end="")
year = int (input())
leap = False
if (year%4 == 0):
    if (year%100 != 0):
        leap = True
    else:
        if (year%400 == 0):
            leap = True

if (leap == True):
    print (year, " is a leap year.")
else:
    print (year, " is not a leap year.")

Please simplify the program and use one “if” statement only.
'''
print ("Please input the year ", end="")
year = int(input())

if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
    print(year, " is a leap year.")
else:
    print(year, " is not a leap year.")
