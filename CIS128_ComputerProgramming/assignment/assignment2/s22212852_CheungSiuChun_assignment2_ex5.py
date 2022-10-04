'''
Course: CIS 128 - Coumputer Programming 1
Assignment 2
Date: 04/10/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercise 5: Average of Three Integers
Write a program to ask the user to input three integers.
Computes and display the average of the three integers.
The program should show clear instructions to tell the user what to input and what is the output.
You may assume the average is a floating point number.
'''

# Describe the purpose of the program
print("-- Calculate the average of three integers --")

# Asking Input from user
int_1 = int(input("Please type in the first integer : "))
int_2 = int(input("Please type in the second integer : "))
int_3 = int(input("Please type in the third integer : "))

# calculate the average of the three numbers
average = (int_1+int_2+int_3)/3.0

# showing 5 significant figures for the average
print(f'The average of the three intergers: {average:.5f}')