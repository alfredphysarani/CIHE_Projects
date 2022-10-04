'''
Course: CIS 128 - Coumputer Programming 1
Assignment 3
Date: 05/10/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercise 4: Write a program to ask the user to input the co-ordinates of the three angles
of a triangle. The program needs to tell the user whether the triangle is an acute-angled 
triangle. Consider the Cosine Law or other more effective methods.
'''

# State the purpose of program
print("-- Acute-angled triangle determination from x, y coordinate of three vertices --")

x_a = float(input("Please input the x coordinate of vertice A of the triangle: "))
y_a = float(input("Please input the y coordinate of vertice A of the triangle: "))
x_b = float(input("Please input the x coordinate of vertice B of the triangle: "))
y_b = float(input("Please input the y coordinate of vertice B of the triangle: "))
x_c = float(input("Please input the x coordinate of vertice C of the triangle: "))
y_c = float(input("Please input the y coordinate of vertice C of the triangle: "))

# calculate the length of side AB, side BC and side CA
sqr_len_AB = (x_a - x_b)**2 + (y_a - y_b)**2
sqr_len_BC = (x_b - x_c)**2 + (y_b - y_c)**2
sqr_len_CA = (x_c - x_a)**2 + (y_c - y_a)**2

'''
According to the property of cos(C), if 0 < C < pi/2, then 1 > cos(C) > 0.
By consine law, cos(C) = (a^2 + b^2 - c^2)/2ab, where a > 0, b > 0 and c > 0
C is an acute-angle if 0 < cos(C) < 1 (i.e. a^2 + b^2 > c^2)
C is an obtuse-angle if -1 < cos(C) < 0 (i.e. a^2 + b^2 < c^2)

For an acute-angled triangle, a^2 + b^2 > c^2, a^2 + c^2 > b^2 and b^2 + c^2 > a^2
'''

if (sqr_len_AB + sqr_len_BC > sqr_len_CA) and (sqr_len_AB + sqr_len_CA > sqr_len_BC) and (sqr_len_BC + sqr_len_CA > sqr_len_AB):
    print(f"The triangle with coordinates ({x_a}, {y_a}), ({x_b}, {y_b}), ({x_c}, {y_c}) is an acute-angled triangle.")
else:
    print(f"The triangle with coordinates ({x_a}, {y_a}), ({x_b}, {y_b}), ({x_c}, {y_c}) is NOT an acute-angled triangle.")


