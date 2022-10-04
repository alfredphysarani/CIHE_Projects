'''
Course: CIS 128 - Coumputer Programming 1
Assignment 2
Date: 04/10/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercise 6: cm to Feet and Inches Conversion for Height 
Write a program that asks the user to input the height of a person in cm.
Convert the height from cm to feet and inches.
The program should show a clear instruction to tell the user what to input and what are the outputs in correct units. 
The input is a floating point number, the number of feet is an integer and the number of inches is a floating point number rounded up to 1 decimal point.

'''

# Describe the purpose of the program
print("-- Conversion of height from cm to Feet (ft) and Inches (in) --")

# Asking Input from user
h_cm = float(input("Please type in the height in the unit of cm: "))

# covert the height in the unit of inch
total_h_inch = h_cm/2.54

# finding the number of full feet  
h_feet = total_h_inch // 12

# calculating the inch remaining after being converted to feet
h_inch = total_h_inch - 12*h_feet

# Output the height in the format of x ft y in
print(f"The height of {h_cm} cm is equivalent to {int(h_feet)} ft {round(h_inch, 1)} in.")


