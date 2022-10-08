'''
Course: CIS 128 - Coumputer Programming 1
Assignment 4
Date: 09/10/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercise 3: Write a Python program that accepts a string and calculate the number of digits and letters.
Note: Use string built-in methods: isdigit() and isalpha()
Test case:  Input string: Python3.0
            Output: 6 letters, 2 digits
'''

s = str(input("Please input a string: "))

n_digit = 0
n_letter = 0

for char in s:
    if char.isdigit():
        n_digit += 1
    elif char.isalpha():
        n_letter += 1

print(f"{n_letter} letter(s), {n_digit} digit(s)")
