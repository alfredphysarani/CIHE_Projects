'''
Course: CIS 128 - Coumputer Programming 1
Assignment 6
Date: 06/11/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercies 2:
Write a program to get a number of numeric values in a line.  Print the min, max and mean of the numbers.
Numbers? 1 2 3 4
Min = 1.0
Max = 4.0
Mean = 2.5
'''

print("Programme: Afternoon greets to names")
numbers = input("Please input multiple numbers and use space to separate each number: ")

def number_list_analysis(numbers: str):
    num_list = []
    for num in numbers.split(" "):
        num_list.append(float(num))

    print(f"Min = {min(num_list)}")
    print(f"Max = {max(num_list)}")
    print(f"Mean = {sum(num_list)/len(num_list)}")

number_list_analysis(numbers)