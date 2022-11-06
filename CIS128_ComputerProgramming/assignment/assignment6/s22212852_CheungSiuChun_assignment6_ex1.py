'''
Course: CIS 128 - Coumputer Programming 1
Assignment 6
Date: 06/11/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercies 1:
Write a program to get a number of names, separated by spaces.  Greet each one of them. 
Names? Peter Mary Paul
Good afternoon, Peter!
Good afternoon, Mary!
Good afternoon, Paul!
Hint: should input a string and convert the string to list by using split() function.
'''

print("Programme: Afternoon greets to names")
names = input("Please input name(s) to be greeted and use space to separate each name: ")

def afternoon_greet(names: str):
    for name in names.split(" "):
        print(f"Good afternoon, {name}!")

afternoon_greet(names)
