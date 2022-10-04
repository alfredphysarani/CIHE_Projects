'''
Course: CIS 128 - Coumputer Programming 1
Assignment 2
Date: 04/10/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercise 6: Celsius to Fahrenheit Conversion for Temperature
Write a program to ask the user to input the temperature in degree Celsius (oC).
Convert the temperature input to degree Fahrenheit (oF) using the following formula.

degF = degC x 1.8 + 32

The program should show a clear instruction to tell the user what to input and what is the output in the correct unit.
You may assume all the numbers are floating point numbers.
The results should be rounded to 1 decimal digit. The following is an example output:

37.5 (C) = 99.5 (F)

At what temperature that it will be the same in both units?
You may use the program to estimate.
'''

# Describe the purpose of the program
print("-- Conversion from temperature in degree Celsius to degree Fahrenheit --")

# Asking Input from user
deg_c = float(input("Please type in temperature in the unit of degree Celsius: "))

# calculate the degree Fahrenheit from degree Celsius
deg_f = deg_c * 1.8 + 32.0

# output: equivalent degree Fahrenheit
print(f'The corresponding temperature in degree Fahrenheit: {deg_f} degree Fahrenheit')

'''
To estimate the temperature that is equivalent in both units, it is equivalent to solve the following equations:
    c = f           --- eq. 1
    f = 1.8c + 32   --- eq. 2

by substituting c as f in equation 2:
    f = 1.8f + 32
    - 0.8f = 32
'''
# calculate the temperature where it is the same for both unit
eq_temp = -32.0/(0.8)
print(f"When the temperature in degree Celsius equals to {eq_temp} oC, the temperature in degree Fahrenheit is also {eq_temp} oF.")

