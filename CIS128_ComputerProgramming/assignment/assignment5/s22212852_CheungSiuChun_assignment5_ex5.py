'''
Course: CIS 128 - Coumputer Programming 1
Assignment 5
Date: 03/11/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercise 5: 
Write a guess number game. The output may be as follows:
'''
from random import randint
from math import log, ceil

def bound_input_validator():
    valid = False
    while valid == False:
        low_bound = int(input("Enter Lower bound:"))
        up_bound = int(input("Enter Upper bound:"))
        if up_bound > low_bound:
            valid = True
        else:
            print("The lower bound must be smaller than upper bound. Please re-enter again.")
    
    return low_bound, up_bound

def min_guess(low_bound, up_bound):
    num = up_bound - low_bound + 1
    return ceil(log(num)/log(2))

def number_guess(low_bound, up_bound, min_allow):
    ans = randint(low_bound, up_bound)
    bingo = False
    n_tries = 0
    
    max_guess = up_bound
    min_guess = low_bound
    while bingo == False:
        valid = False
        while valid == False:
            x = int(input(f"Guess a number between {min_guess} and {max_guess} (Remaing no. of trials = {min_allow-n_tries}): \n"))
            if (x <= max_guess) and (x >= min_guess):
                valid = True
            elif (x > max_guess):
                print(f"The guess is greater than the upper guess limit: {max_guess}, Please re-enter again.")
            elif (x < min_guess):
                print(f"The guess is smaller than the lower guess limit: {min_guess}, Please re-enter again.")
        
        n_tries += 1
        if x > ans:
            print("Your guess is greater than the target.")
            max_guess = x - 1
        elif x < ans:
            print("Your guess is smaller than the target.")
            min_guess = x + 1
        else:
            bingo = True
            print(f"Good job! You did it in {n_tries} guesses.")
            break

        if n_tries == min_allow:
            print(f"You have used up the allowed number of trials. The target is {ans}.")
            break

low_bound, up_bound = bound_input_validator()
min_allow = min_guess(low_bound, up_bound)
number_guess(low_bound, up_bound, min_allow)







