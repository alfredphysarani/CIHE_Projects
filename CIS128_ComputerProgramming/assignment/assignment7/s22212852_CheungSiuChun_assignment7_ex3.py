'''
Course: CIS 128 - Coumputer Programming 1
Assignment 7
Date: 14/11/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercies 3:
Write a program to allow the user to input the principal P, the interest rate r (in percentage) and the number of periods n. The program then calculates the sum S of principal and interest through a function.

S=P\times\left(1+r\right)^n

The example inputs and outputs are like that:

Please input the principal: 10000
Please input the interest rate in percentage: 10
Please input the number of periods: 10
The sum of principal and interest after 10 periods is $25937.4246.
'''

print("Programme: calculater for sum of principal and interest under compound interst")
p = float(input("Please input the principal: "))
r = float(input("Please input the interest rate in percentage: "))
n = float(input("Please input the number of periods: "))

def sum_principal_int(p, r, n):
    return p*(1+r/100)**n

print(f"The sum of principal and interest after 10 periods is ${sum_principal_int(p, r, n):.4f}.") 