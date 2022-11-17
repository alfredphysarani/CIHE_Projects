'''
Course: CIS 128 - Coumputer Programming 1
Assignment 5
Date: 03/11/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercise 2: 
Write a program to find the length of a string. (3 different methods)
a. Using built-in function
b. Using for-Loops
c. Using while-Loop
'''

txt = str(input("Please input a string: "))
# a. Using built-in function
print(f"The length of the string by built-in function: {len(txt)}")

# b. Using for-Loops

def for_loop_length_str(txt):
    n = 0
    for char in txt:
        n += 1
    return n

print(f"The length of the string by for-Loops: {for_loop_length_str(txt)}")

#c. Using while-Loops

def while_loop_length_str(txt):
    n = 0
    while txt[n:]:
        n += 1

    return n

print(f"The length of the string by while-Loops: {while_loop_length_str(txt)}")

