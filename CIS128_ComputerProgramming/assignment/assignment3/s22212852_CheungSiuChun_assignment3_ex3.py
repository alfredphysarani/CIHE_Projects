'''
Course: CIS 128 - Coumputer Programming 1
Assignment 3
Date: 05/10/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercise 3: Write a program to ask the user to input the lengths of the three sides (a, b and c) of a triangle.
The program needs to tell the user whether the triangle is a right-angled triangle. 
Hint: consider the Pythagoras' Theorem.
'''

# State the purpose of program
print("-- Right-angled triangle determination from length of three sides --")

len_a = float(input("Please input the length of side a of the triangle: "))
len_b = float(input("Please input the length of side b of the triangle: "))
len_c = float(input("Please input the length of side c of the triangle: "))

if ((len_a**2 + len_b**2) == len_c**2) or ((len_a**2 + len_c**2) == len_b**2) or ((len_b**2 + len_c**2) == len_a**2):
    print(f"The triangle with length of three sides ({len_a}, {len_b}, {len_c}) is a right-angled triangle")
else:
    print(f"The triangle with length of three sides ({len_a}, {len_b}, {len_c}) is NOT a right-angled triangle")
