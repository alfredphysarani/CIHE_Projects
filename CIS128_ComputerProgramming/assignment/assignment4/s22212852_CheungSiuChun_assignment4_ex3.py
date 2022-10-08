'''
Course: CIS 128 - Coumputer Programming 1
Assignment 4
Date: 09/10/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercise 3: Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note: Use 'continue' statement.
Expected Output: 0 1 2 4 5

'''

for n in range(0, 7):
    if n > 0 and n%3 == 0:
        continue
    print(n)






