'''
Course: CIS 128 - Coumputer Programming 1
Assignment 3
Date: 05/10/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercise 2: Write a program to ask the user to input the mark of a subject. 
The program needs to print the grade of the subject according to the following criteria:
Grade is “F” if mark < 50
Grade is “E” if mark >= 50 and mark < 60
Grade is “D” if mark >= 60 and mark < 70
Grade is “C” if mark >= 70 and mark < 80
Grade is “B” if mark >= 80 and mark < 90
Grade is “A” if mark >= 90
'''

# State the purpose of program
print("-- Convert marks into Grade of a subject --")

mark = float(input("Please input the mark of a subject: "))

if (mark < 50):
    grade = "F"
elif (mark < 60):
    grade = "E"
elif (mark < 70):
    grade = "D"
elif (mark < 80):
    grade = "C"
elif (mark < 90):
    grade = "B"
else:
    grade = "A"

print(f"The grade of the subject: {grade}")