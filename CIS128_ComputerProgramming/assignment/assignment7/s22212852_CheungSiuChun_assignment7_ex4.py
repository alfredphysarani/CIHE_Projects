'''
Course: CIS 128 - Coumputer Programming 1
Assignment 7
Date: 14/11/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercies 4:
Write a program to allow the user to input a positive integer n. The program then calls a function to check whether the number is a prime number. If the number is a prime number, the function should return a “True”, otherwise it should return a “False”.  The main program should print the result based on the returned value. The example inputs and outputs are as follows:

Please input an integer: 37
37 is a prime number.
Please input an integer: 49
49 is not a prime number.
'''
from math import ceil

print("Programme: Prime Number Classifier")

n = 0
while n <= 0:
    n = int(input("Please input a positive interger: "))

    if n <= 0:
        print("The input is not a positive integer.")


def prime_detector(n: int):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n != 2 and n != 5 and str(n)[-1] in ["2", "4", "6", "8", "5", "0"]: # integer ending with 2, 4, 5, 6, 8, 10 must not be a prime
        return False
    else:
        i = 2
        while (i != ceil(n/2)):
            if (n % i == 0):
                return False
            else:
                i += 1
        return True



if prime_detector(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
