'''
Course: CIS 128 - Coumputer Programming 1
Assignment 2
Date: 04/10/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercise 3:
Write a program to get the radius and slant side length of a cone. 
Compute and display the surface area and volume of the cone as in sample output.
'''

from math import pi, sqrt

# Describe the purpose of the program
print("-- Calculate the Area and Circumference of a Circle --")

# Asking Input from user
r_cone = float(input("Please type in the base radius of the cone and press enter to submit : "))
s_cone = float(input("Please type in the slant side of the cone and press enter to submit : "))

'''
Volume of cone can be calculated as:
V   = 1/3 * pi * r^2 * h
    = 1/3 * pi * r^2 * sqrt(s^2 - r^2)
''' 
vol_cone = pi * r_cone**2 * sqrt(s_cone**2 - r_cone**2) * 1.0/3
'''
Volume of cone can be calculated as:
A   = pi * r^2 + pi * s^2 * ((2*pi*r)/(2*pi*s))
    = pi * r * (r + s)
'''
surface_area_cone = pi * r_cone * (r_cone + s_cone)

# Output the volume and surface area of the cone
print(f"The volume of the cone: {vol_cone:.2f}")
print(f"The surface area of the cone: {surface_area_cone:.4f}")
