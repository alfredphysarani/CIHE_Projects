'''
Course: CIS 128 - Coumputer Programming 1
Assignment 7
Date: 14/11/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercies 2:
Write a program to allow the user to input the height h of a hollow triangle. Then the program calls a function to print the triangle. The following are examples of inputs and outputs.

When h=0, print nothing.
When h=1, the output is:
*
When h=2, the output is:
 *
***
When height=3, the output is:

  *
 * *
*****
'''

print("Programme: isoceles triangle Printer")
h = int(input("Please input the height (h) of the triangle: "))

def triangle_printer(h: int):
    if h <= 0:
        return
    else:
        for i in range(1, h+1):
            if i == 1:
                print(" "*(h-1) + "*" + " "*(h-1))
            elif i > 1 and i < h:
                print(" "*(h-i) + "*"+ " "*(2*i-3) + "*" + " "*(h-i))
            elif i == h:
                print("*"*(2*h-1))

triangle_printer(h)
