'''
Course: CIS 128 - Coumputer Programming 1
Assignment 9
Date: 03/12/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Write a program to read a file “Random_numbers.txt”. The file stores 1000 numbers with 
values from 1 to 1000. Read these number into the computer and sort them. Find the mean, 
median, mode(s) and standard deviation of the 1000 numbers.
Mean is the average of the 1000 numbers. Mode is the number appears most frequently. If 
there are more than one number appears the same highest frequency, then there are more than 
one modes. The median in this case is the average of the 500th and 501st number. The formula 
of the standard deviation is as follows:

s.d. = sqrt(summation from 1 to n (x_i - mean(x))**2 / (n-1))

Please use the basic instructions of Python to solve the problem but NOT calling the 
functions from the Python.
'''

import os
from math import sqrt

with open(os.path.join(os.getcwd(), "Random_number.txt"), mode="r", encoding='utf-8') as f:
    raw_data = f.readlines()

def raw_data_handler(data: list):
    num_list = []
    sorted_num_list = []
    histo_dict = {}
    for n in data: # O(n)
        num_list.append(float(n.strip("\n")))
    
    # finding frequency of each number: O(n)
    for num in num_list: 
        if num not in histo_dict:
            histo_dict[num] = 1
        else:
            histo_dict[num] += 1
    
    # not using list.sort() to sort the list of numbers: O(n)
    i = 0.0
    while len(sorted_num_list) < len(num_list): # sorted list must have the same length as the unsorted list
        for key in histo_dict.keys():
            if i == key:
                for freq in range(0, histo_dict[i]):
                    sorted_num_list.append(i)
            
        i += 1
    
    # testing area
    #num_list.sort()
    #assert sorted_num_list == num_list
    
    return sorted_num_list, histo_dict

def mean_calc(data: list):
    sum = 0
    for n in data:
        sum += n
    
    return sum/len(data)

def median_finder(sorted_data: list):
    median = 0
    if len(sorted_data) % 2 == 0:
        median = (sorted_data[int(len(sorted_data)/2-1)] + sorted_data[int(len(sorted_data)/2)])/2
    else:
        median = sorted_data[int((len(sorted_data)/2-0.5))]
    
    return median

def mode_finder(histo_dict: dict):
    max_freq = 0
    # not using the list.max() functions (i.e. hist_dict.values().max() can find the max value easily)
    for key in histo_dict.keys():
        if histo_dict[key] > max_freq:
            mode_list = []
            max_freq = histo_dict[key]
            mode_list.append(key)
        elif histo_dict[key] == max_freq:
            mode_list.append(key)
    
    return mode_list

def sd_calc(data: list):
    # not using the sum function
    sqr_mean_sum = 0
    mean = mean_calc(data)
    for num in data:
        sqr_mean_sum += (num - mean)**2
    
    return sqrt(sqr_mean_sum/(len(data)-1))


    
proc_list, histo_dict = raw_data_handler(raw_data)
print(f"The mean of the numbers in the file: {mean_calc(proc_list)}")
print(f"The median of the numbers in the file: {median_finder(proc_list)}")
print(f"The mode(s) of the numbers in the file: {mode_finder(histo_dict)}")
print(f"The standard deviation of the numbers in the file: {sd_calc(proc_list)}")


'''
Testing block
import numpy as np
assert mean_calc(proc_list) == np.mean(proc_list)
assert median_finder(proc_list) == np.median(proc_list)
assert sd_calc(proc_list) == np.std(proc_list, ddof=1)
'''





