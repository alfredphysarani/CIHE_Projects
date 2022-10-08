'''
Course: CIS 128 - Coumputer Programming 1
Assignment 4
Date: 09/10/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercise 2: A quadratic equation is written as follow:

ax^2+bx+c=0

a is not zero. To find the roots x1 and x2 of the equation, we use the following formula:

x_1= -b + \sqrt(b^2-4ac)/2a
x_2= -b - \sqrt(b^2-4ac)/2a

The expression underneath the square root sign is called the discriminant Δ (delta) of the quadratic equation.
It is defined as follow:

Δ =b^2-4ac

There are three cases of Δ:
Δ < 0, there is no real root
Δ = 0, there is one unique real root (x1 = x2)
Δ > 0, there are two real roots

Write a program to allow the user to input the three coefficients of a quadratic equation,
check the three cases of the Δ and display a message to user.
Then calculate and display the root(s) if there exists.
'''

from math import sqrt

print("Calculator for roots of qudratic equation, ax^2 + bx + c = 0")
a = float(input("Please input the coefficient of x^2, a: "))
b = float(input("Please input the coefficient of x, b: "))
c = float(input("Please input the coefficient, c: "))

delta = b**2 - 4*a*c

if (delta < 0):
    print(
        f"The discriminant (b^2 -4ac) is {delta}, which is smaller than zero, so there is no real root for the quadratic equation {a}x^2 + {b}x + {c}."
        )

elif (delta == 0):
    print(
        f"The discriminant (b^2 -4ac) is {delta}, so there is only one real root for the quadratic equation {a}x^2 + {b}x + {c}."
        )
    root = -b / (2*a)
    print(f"The root x for quadratic equation {a}x^2 + {b}x + {c} is {root}.")
else:
    print(
        f"The discriminant (b^2 -4ac) is {delta}, which is greater than zero, so there are two real roots for the quadratic equation {a}x^2 + {b}x + {c}."
        )
    root_1 = (-b + sqrt(delta)) / (2*a)
    root_2 = (-b - sqrt(delta)) / (2*a)
    print(f"The first root (x_1) for quadratic equation {a}x^2 + {b}x + {c} is {root_1}.")
    print(f"The second root (x_2) for quadratic equation {a}x^2 + {b}x + {c} is {root_2}.")






