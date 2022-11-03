'''
Course: CIS 128 - Coumputer Programming 1
Assignment 5
Date: 03/11/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercise 3: 
Write a program to get a number n (between 1 and 10, inclusively) from 
user's input. Then, print a trapezium accordingly.
'''

input_valid = False

while input_valid == False:
    n = int(input("Please input a number between 1 and 10: "))
    
    if n <= 10 and n >=1:
        input_valid = True
    else:
        print("The input is not within 1 to 10.")

def trapezium(n):
    print("*" * n)

    for l in range (0, n-2):
        print("*" + " " * (n - 1 + l) + "*")

    if n > 1:
        print("*" * (2*n - 1))

trapezium(n)



