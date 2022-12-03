'''
Course: CIS 128 - Coumputer Programming 1
Assignment 8
Date: 28/11/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Write a Python program to read a file line by line store it into a variable.
'''

data_list=["a", "bc", "def", "ghij"]

with open("output.txt", "w", encoding="utf-8") as f:
    for item in data_list:
        f.write(item+"\n")









