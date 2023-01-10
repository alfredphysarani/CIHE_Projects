'''
Exercise 1: 
Write a Python function to multiply all the numbers in a list.
'''
def multiply(num_list: list):
    product = 1
    for n in num_list:
        product *= n
    
    return product

test_list = [8, 2, 3, -1, 7]
print(multiply(test_list))

'''
Exercise 2:
Given a number N and power P, \
    the task is to find the power of a \
    number ( i.e. NP) using recursion.
'''

def power_calc(N, P):
    if P == 0:
        return 1
    else:
        return power_calc(N, P-1)*N

print(power_calc(2, 3))
print(power_calc(5, 2))
print(power_calc(6, 1))
print(power_calc(7, 0))

'''
Exercise 3:
Write a Python program which takes two digits m (row) and n 
(column) as input and generates a two-dimensional array. The 
element value in the i-th row and j-th column of the array should 
be i*j.
'''

'''
row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of column: "))

def twoD_array_build(m, n):
    return [[i*j for i in range(n)] for j in range(m)]

print(twoD_array_build(row_num, col_num))
'''

'''
Exercise 4:
Write a Python program to create the multiplication table (from 1 to 10) of a number.
'''

'''
number = int(input("Input a number: "))

def multi_table(number: int):
    for i in range(1, 11):
        print(f"{number} x {i} = {number*i}")

multi_table(number)
'''

'''
Exercise 5:
Write a Python program to check the validity of a password (input from users).
'''

'''
import re

password = str(input("Please input your password: "))

def pw_validator(password):
    if len(password) < 6 or len(password) > 16:
        print("Not a Valid Password")
        return False
    elif not re.search("[a-z]", password):
        print("Not a Valid Password")
        return False
    elif not re.search("[A-Z]", password):
        print("Not a Valid Password")
        return False
    elif not re.search("[0-9]", password):
        print("Not a Valid Password")
        return False
    elif not re.search("[$#@]", password):
        print("Not a Valid Password")
        return False
    else:
        print("Valid Password")
        return True

pw_validator(password)
'''

'''
assert pw_validator('1aA#ss') == True
assert pw_validator('1aA#s') == False
assert pw_validator('1aA#ss1aA#ss') == True
assert pw_validator('1aA#ss1aA#ss3') == False
assert pw_validator('1aA3ss') == False
assert pw_validator('1abc#@') == False
assert pw_validator('1CA#BB') == False
assert pw_validator('abc$FG') == False
assert pw_validator('123456') == False
'''

'''
Exercise 6
Write a Python program to check a triangle is equilateral, isosceles or scalene.
'''

'''
print("Please input the length of three sides of the triangle: ")
x = float(input("Please input for the length first side(x): "))
y = float(input("Please input for the length second side(y): "))
z = float(input("Please input for the length third side(z): "))

def tri_checker(x, y, z):
    if x == y and y == z:
        print("The triangle is a equilateral triangle.")
    elif x == y or y == z or z == x:
        print("The triangle is a isosceles triangle.")
    else:
        print("The triangle is a scalene triangle.")

tri_checker(x, y, z)
'''

'''
Exercise 7
Write a Python program to check whether a specified value is contained in a group of values.
'''

def exist_check(val, val_group: list):
    for item in val_group:
        if val == item:
            return True
    
    return False

print(exist_check(3, [1, 5, 8, 3]))
print(exist_check(2, [1, 5, 8, 3]))

'''
Exercise 8
Write a Python program to concatenate all elements in a list into a string and return it.
'''
def concatenate(input_list: list):
    result = ""
    for item in input_list:
        result += str(item)
    
    return result

print(concatenate([1, 5, 12, 2]))

'''
Exercise 9
Write a Python program to display your details like name, age, 
address in three different lines.
'''

def personal_info(name, age, address):
    print(f"Name: {name}\nAge: {age}\nAddress: {address}")

personal_info("Alfred", 29, "Quarry Bay, Hong Kong")

'''
Exercise 10
Write a Python program to compute the amount of the debt in n 
months. The borrowing amount is $100,000 and the loan adds 5% 
interest of the debt and rounds it to the nearest 1,000 above month by 
month.
'''

def round_up_thousand(num):
    if num%1000:
        return(1+num//1000)*1000
    else:
        return num

def interest_calc(init_debt, n):
    if n == 0:
        return round_up_thousand(init_debt)

    return interest_calc(round_up_thousand(init_debt*(1+0.05)), n-1)

print(interest_calc(100000, 7))