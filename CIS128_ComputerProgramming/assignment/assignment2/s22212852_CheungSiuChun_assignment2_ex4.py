'''
Course: CIS 128 - Coumputer Programming 1
Assignment 2
Date: 04/10/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercise 4: Area and Circumference of a Circle
Write a program to ask the user to input the radius of a circle in cm.
Computes the area and the circumference of the circle.
The program should show clear instructions to tell the user what to input and what are the outputs.
The outputs should show the correct units. 
You may assume all the numbers are floating point numbers and the outputs should be rounded up to 2 decimal digits.
'''

from math import pi

# Describe the purpose of the program
print("-- Calculate the Area and Circumference of a Circle --")

# Asking Input from user
radius = float(input("Please type in the radius of the circle in the unit of cm and press enter to submit : "))

# calculate the area of circle with radius
area = pi*radius**2
# calculate the circumference of circle with radius
circ = 2*pi*radius

# Output the area and circuference in 2 decimal places
print(f"The area of circle: {round(area, 2)} cm2.")
print(f"The circumference of the circle: {round(circ, 2)} cm")