'''
Course: CIS 128 - Coumputer Programming 1
Assignment 7
Date: 14/11/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercies 1:
Write a program to allow the user to input the width w and height h of a hollow rectangle. Then the program calls a function to print the rectangle. The following are examples of inputs and outputs.

When either width or height is 0, or both of width and height are 0, print nothing.
When w=1 and h=1, the output is:
*
When w=1 and h=2, the output is:
*
*
When w=2 and h=2, the output is:
**
**
When w=5 and h=3, the output is:
*****
*   *
*****
'''

print("Programme: Rectangle Printer")
w = int(input("Please input the width (w) of the rectangle: "))
h = int(input("Please input the height (h) of the rectangle: "))

def rectangle_printer(w: int, h: int):
    if w <= 0 or h <= 0:
        return
    else:
        for i in range(1, h+1):
            if i == 1 or i == h:
                print("*"*w)
            elif i > 1 and i < h:
                print("*"+" "*(w-2)+"*")

rectangle_printer(w, h)
