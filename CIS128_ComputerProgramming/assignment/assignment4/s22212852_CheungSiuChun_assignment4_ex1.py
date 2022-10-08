'''
Course: CIS 128 - Coumputer Programming 1
Assignment 4
Date: 09/10/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercise 1: The following program print the “*” according to the input number n,
where is the number of rows of “*”.

print ("Please input the number of rows of * to print ", end="")
n = int (input())
j = 1
while j <= n:
    i = 1
    while i <= j:
        print ("*", end = "")
        i += 1
    print ("")
    j += 1

When n = 4, the output is as follow:
*
**
***
****

(a) Using the string operation and one while loop only to rewrite the about program.

stars = stars + “*”	#Add one more “*” to the string “stars”
'''

print ("Please input the number of rows of * to print ", end="")
n = int (input())

j = 1
stars = ""

while j <= n:
    stars = stars + "*"
    print(stars)
    j += 1

'''
(b) Using another string operation and one while loop only to rewrite the about program.

print (stars[:j])	#j is the number of “*” to be printed

'''

print ("Please input the number of rows of * to print ", end="")
n = int (input())

j = 1
stars = n * "*"

while j <= n:
    print(stars[:j])
    j += 1
