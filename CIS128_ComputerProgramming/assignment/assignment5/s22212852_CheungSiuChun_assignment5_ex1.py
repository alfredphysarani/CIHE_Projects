'''
Course: CIS 128 - Coumputer Programming 1
Assignment 5
Date: 03/11/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercise 1: Write a program to read in a string and print it in reverse order.
'''

print("Programme: Printing reversed string")
txt = input("Please input a string: ")

def reverse_string(txt: str):
    print(txt[::-1])
    return txt[::-1]

reverse_string(txt)

