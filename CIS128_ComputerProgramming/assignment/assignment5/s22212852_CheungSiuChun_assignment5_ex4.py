'''
Course: CIS 128 - Coumputer Programming 1
Assignment 5
Date: 03/11/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercise 4: 
 Write a Python function to find the Max of three numbers.
'''

num_1 = float(input("Please input the 1st number: "))
num_2 = float(input("Please input the 2nd number: "))
num_3 = float(input("Please input the 3rd number: "))

def max_num(num_1, num_2, num_3):
    if (num_1 >= num_2) and (num_1 >= num_3):
        max = num_1
    elif (num_2 >= num_1) and (num_2 >= num_3):
        max = num_2
    else:
        max = num_3
    
    return max

print(max_num(num_1, num_2, num_3))



