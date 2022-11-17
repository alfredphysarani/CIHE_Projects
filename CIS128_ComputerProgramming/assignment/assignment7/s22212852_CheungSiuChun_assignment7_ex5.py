'''
Course: CIS 128 - Coumputer Programming 1
Assignment 7
Date: 14/11/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercies 5:
Write a program to allow the user to input 2 integers n and r. Then the program passes the two integers to a function to calculate the nCr, which is the number of combinations of choosing r items from n items. Here r must be less than or equal to n. The function of nCr is defined as follows:
nCr=\frac{n!}{r!\left(n-r\right)!}

where n! is named as factorial, defined as follows:

In this program, please define two functions: nCr and factorial. The main program calls the nCr function and the nCr function calls the factorial function 3 times. The example input and output are as follows:
'''
from math import ceil

print("Programme: Combination nCr calculator")

n = -1
r = -1
while n < 0 or r < 0 or r > n:
    n = int(input("Please input n: "))
    r = int(input("Please input r: "))

    if n <= 0 or r <= 0:
        print("The input is a negative integer.")
    elif r>n:
        print("n must be greater or equal to r.")



def factorial(num):
    if num == 0: # by definition of factorial
        return 1
    else:
        result = 1
        for n in range(1, num+1):
            result *= n
        return result

def combination_calc(n, r):
    return int(factorial(n)/(factorial(r)*factorial(n-r))) #combination must be an integer

print(f"{n}C{r} is equal to {combination_calc(n, r)}")

