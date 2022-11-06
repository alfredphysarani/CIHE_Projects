'''
Course: CIS 128 - Coumputer Programming 1
Assignment 6
Date: 06/11/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercies 4:
Write a function prime() to take n as input, and returns a list of all prime numbers smaller than n.

Assumption: the prime numbers print out are positive?
'''

from math import ceil

print("Programme: all prime numbers smaller than n.")
n = float(input("Please input a number: "))

def prime(n: float):
    prime_list = list(range(2, ceil(n)))
    #loop_count = 0 # to check performance
    for num in range(2, ceil(n)): # O(n^2) method, kind of slow
        i = 2
        while (i <= num/2): # the reason of using num/2 is based on the fact that num > num/2 will not be a factor of num. It can reduce the number of iteration.
            #loop_count += 1
            if (num % i == 0):
                prime_list.remove(num)
                i += 1
                if i % 2 == 0: # since even number is a factor of 2, reduce iteration if i is an even number, add 1 to become odd
                    i += 1
                break
            else:
                i += 1
                if i % 2 == 0: # since even number is a factor of 2, reduce iteration if i is an even number, add 1 to become odd
                    i += 1
                continue

    #print(f"The programme uses loops: {loop_count} to get a prime number list smaller than {n}.")        
    #print(len(prime_list))
    return prime_list


print(prime(n))