'''
Course: CIS 128 - Coumputer Programming 1
Assignment 1
Date: 04/10/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Question 1
Write a program to:
1. get the radius and height of a cylinder (with appropriate messages). 
2. Then, compute the volume and surface area of it, and print the results to the screen.
'''

from math import pi

def userInputFilter(para_name):
    # para_name = name of the parameter to get
    validator = False
    while validator == False:
        # using try and except to avoid invalid input from user
        try:
            param = input(f"Please type in the {para_name} of the cylinder (or type x to exit) and press enter to submit : ")
            if param == 'x':
                exit()
            else:
                param = float(param)
        except Exception:
            print("Invalid Input: Please input a zero, positive decimals or positive intergers. \n")
        else:
            # using try and except to avoid invalid input from user
            if param < 0:
                print("Negative Number: Please input a zero, positive decimals or positive intergers. \n")
            else:
                validator = True
    return param

def volume_calc_cylinder(r, h):
    '''
        calculate the volume of the cylinder with radius r and height h
        V = pi x r^2 x h 
    '''
    return pi * h* r**2

def surf_area_calc_cylinder(r, h):
    '''
        calculate the surface area of the cylinder with radius r and height h
        A = 2 x pi x r x h + 2 x pi x r^2 
    '''
    return (r*2*h*pi) + (2*pi*r**2)

if (__name__== '__main__'):
    # greeting to user
    print("-- Calculator for Volume and Surface area of a Cylinder -- \n")
    r = userInputFilter('radius')
    h = userInputFilter('height')

    print(f"The radius of the cylinder input: {r}")
    print(f"The height of the cylinder input: {h}\n")

    print(f"The volume of the cylinder: {volume_calc_cylinder(r, h)}")
    print(f"The surface area of the cylinder: {surf_area_calc_cylinder(r, h)}\n")


    
    
