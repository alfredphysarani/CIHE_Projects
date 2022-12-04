'''
Course: CIS 128 - Coumputer Programming 1
Assignment 9
Date: 03/12/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Write a program to find out all the solutions of the 3 x 3 magic square. You can express the 
matrix as a number. For example, the matrix shown above can be expressed as:
492357816
In the program, you can treat the numbers in the square as digits of a 9-digit number. You 
need to generate different patterns and check whether the pattern is valid. If there are digits 
equal, the pattern is invalid. If the pattern is valid, we need to check when the sums of rows, 
columns and diagonals are all equal. Save the pattern if it is a solution
'''

'''
Using math analysis:
as there are 9 digits (not including 0) and there are 9 GRIDs, the total permuation = 9P9 = 362880

The 3 x 3 grid can be considered as a matrix and consider the symmetry of the matrix arrangement:
(i.e. a the reflective symmetry + rotational symmetry of a square)

The following is a solution (492357816):
4 9 2
3 5 7
8 1 6

rotaional symmetry (1 axis thorugh the center perpendicular to the surface / others are covered by the reflective symmetry)
then the reverse of the digit is also a solution (618753294) [rotational]:
6 1 8
7 5 3
2 9 4
it implies that we can find all the solution between 123456789 to 549876321, then reversing each solution.
Reversing using: int(str(solution)[::-1])

Other rotational solution (276951438), (834159672)
2 7 6  8 3 4
9 5 1  1 5 9
4 3 8  6 7 2
Rotate counter-clockwise by 90-deg (index change): 0->6, 1->3, 2->0, 3->7, 5->1, 6->8, 7->5, 8->2 
Rotate clockwise by 90-deg (index change): 0->2, 1->5, 2->8, 3->1, 5->7, 6->0, 7->3, 8->6

Reflective symmetry (4 axis for a square)
Moreover, the transpose of the matrix is also a solution (438951276) 
4 3 8
9 5 1
2 7 6
Transpose (index change): 1->3, 2->6, 3->1, 5->7, 6->2, 7->5

switching between first row and third row (816357492)/ first column and third column (294753618)
8 1 6  2 9 4
3 5 7  7 5 3
4 9 2  6 1 8
Row Relect (index change): 0->6, 1->7, 2->8, 6->0, 7->1, 8->2
Col Relect (index change): 0->2, 3->5, 6->8, 2->0, 5->3, 8->6

OR transposing along the diagonal from top-right to bottom left (672159834)
6 7 2
1 5 9
8 3 4
Reflect along the diagonal from top-right to bottom left (index change): 0->8, 1->5, 3->7, 5->1, 7->3, 8->0
'''

'''
Define two mode of the game
Mode 1: Show all solution from valid pattern
Mode 2: Accept input from user and determine the whether it is a solution
'''

def permutation(num_string: str, output: str, store_list: list):
    # functions to generate all the 9! combnations of 9 separated digits
    if len(num_string) == 0:
        store_list.append(int(output))
        return

    for n in range(0, len(num_string)):
        left_digits = num_string[0:n]
        right_digits = num_string[n+1:]
        comb = left_digits + right_digits
        permutation(comb, output + num_string[n], store_list)

def magic_checker(num):
    sum_row1 = int(str(num)[0]) + int(str(num)[1]) + int(str(num)[2])
    sum_row2 = int(str(num)[3]) + int(str(num)[4]) + int(str(num)[5])
    sum_row3 = int(str(num)[6]) + int(str(num)[7]) + int(str(num)[8])

    sum_col1 = int(str(num)[0]) + int(str(num)[3]) + int(str(num)[6])
    sum_col2 = int(str(num)[1]) + int(str(num)[4]) + int(str(num)[7])
    sum_col3 = int(str(num)[2]) + int(str(num)[5]) + int(str(num)[8])

    sum_diag1 = int(str(num)[0]) + int(str(num)[4]) + int(str(num)[8])
    sum_diag2 = int(str(num)[2]) + int(str(num)[4]) + int(str(num)[6])

    if sum_row1 == sum_row2 and sum_row1 == sum_row3 and sum_row1 == sum_col1 and sum_row1 == sum_col2 and sum_row1 == sum_col3 and sum_row1 == sum_diag1 and sum_row1 == sum_diag2:
        return True
    else:
        return False

def number_validator(num):
    if not str(num).isnumeric():
        print("Please avoid inputting non-numeric characters")
        return False

    if len(str(num)) != 9:
        print("Please input an integer with 9 places.")
        return False
    
    for digit in str(num):
        if digit == '0':
            print("Please input an integer with digit from (1-9).")
            return False
    
    for i in range(0, 9):
        for j in range (i+1, 9):
            if str(num)[i] == str(num)[j]:
                print("Please input an integer with digit from (1-9) without repeated digits.")
                return False

    return True

print("-- Welcome to Magic Square Checker-- \n")
print("Input A to show all the solutions.")
print("Input B to play the game.")

option = ''
while option != 'A' and option != 'B':
    option = input('Please input (A/B) to select the mode: ')
    option = option.upper()
    
    if option != 'A' and option != 'B':
        print("Please input character A or B")

if option == 'A':
    n = 123456789
    valid_combination =[]
    solution = []
    
    permutation(str(n), "", valid_combination)
    
    for num in valid_combination:
        if magic_checker(num):
            solution.append(num)
        
    print(f"The solutions of magic square: {solution}")
    print(f"The number of solutions: {len(solution)}")

elif option == 'B':
    valid = False
    while valid == False:
        num = input('Please input an 9-digit integer with digit from (1-9): ')

        valid = number_validator(num)
    
    if magic_checker(num):
        print(f"{num} is a solution of the magic square.")
    else:
        print(f"{num} is not a solution of the magic square.")


            
    

    










