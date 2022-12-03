'''
Course: CIS 128 - Coumputer Programming 1
Assignment 8
Date: 28/11/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Write a program to read a file "names.txt".
Read the names on each line.
Then reverse the order of the characters and save it onto a new file called "reverse.txt".
For example, the first line was “Peter”.
It will be changes to “reteP” afterwards.
'''

import os
try:
    f_read = open(os.path.join(os.getcwd(), "name.txt"), mode="r", encoding='utf-8')
except:
    print("Error when opening file.")

try:
    f_out = open(os.path.join(os.getcwd(), "reverse.txt"), mode="w", encoding='utf-8')
    for line in f_read:
        f_out.write(line[::-1].replace("\n", "")+"\n")
except:
    print("Error when opening file.")
finally:
    f_out.close()
    f_read.close()






