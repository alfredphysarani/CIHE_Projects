'''
Course: CIS 128 - Coumputer Programming 1
Assignment 6
Date: 06/11/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercies 3:
Write a function odd() to take n as input, and returns a list of all odd numbers smaller than n.

Assumption: the odd numbers print out are positive?
'''

from math import ceil

print("Programme: all odd numbers smaller than n.")
n = float(input("Please input a number: "))

def odd(n: float):
    return list(range(1, ceil(n), 2))

print(odd(n))
