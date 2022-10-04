'''
Course: CIS 128 - Coumputer Programming 1
Assignment 2
Date: 04/10/2022
Name: Cheung Siu Chun
Student ID: 22212852
'''

'''
Exercise 1: Please do the following conversions:
a. Convert 765(10) into binary, hexadecimal numbers.
b. Convert DA3(16) into binary and decimal numbers.
'''

'''
Ex 1a: hand-division
From Decimal to Binary
2   |765   
2   |382   1
2   |191   0
2   |95    1
2   |47    1
2   |23    1
2   |11    1
2   |5     1
2   |2     1
     1     0

Reading from bottom to up
765 (decimal)   = 1011111101 (binary)

By using the binary form to convert to Hexadecimal numbers
Grouping the binary numbers into group of 4 digits
765 (dec)   = 1011111101 (bin)
            = 0010 1111 1101 (bin)
            = 2(dec) 15(dec) 13(dec)
            = 2FD (hex)

Ex 1b: hand multiplcation
DA3 (hex)   = 13 x 16^2 + 10 x 16^1 + 3 x 16^0
            = 3491 (dec)

DA3 (hex)   = (1101 1010 0011) (bin)
            = 110110100011 (bin)
'''

# Ex 1a: using Python, but not using public library
def dec_to_bin_hex(dec_number):
    dummy = dec_number
    bin_storage = ''
    while dummy >=2:
        remainder = dummy % 2
        bin_storage += str(remainder)
        dummy = dummy // 2
    
    bin_storage += '1'
    bin_form = bin_storage[::-1]
    print(f"The binary form of {dec_number}: {bin_form}")

    if len(bin_form) % 4 != 0:
        zero_missing = 4 - (len(bin_form) % 4)
        bin_form = zero_missing*'0' + bin_form
    
    n = len(bin_form) // 4
    hex_form = ''

    for i in range(0,n*4,4):
        power = 3
        dec_sum = 0
        for digit in bin_form[i:i+4]:
            dec_sum += int(digit)*2**power
            power -= 1
        
        if dec_sum == 10:
            hex_form += 'A'
        elif dec_sum == 11:
            hex_form += 'B'
        elif dec_sum == 12:
            hex_form += 'C'
        elif dec_sum == 13:
            hex_form += 'D'
        elif dec_sum == 14:
            hex_form += 'E'
        elif dec_sum == 15:
            hex_form += 'F'
        else:
            hex_form += str(dec_sum)
    
    print(f"The hexadecimal form of {dec_number}: {hex_form}")

dec_to_bin_hex(765)
'''Output
The binary form of 765: 1011111101
The hexadecimal form of 765: 2FD
'''

dec_to_bin_hex(3491)
'''Output
The binary form of 3491: 110110100011
The hexadecimal form of 3491: DA3
'''

# Ex 1b: using Python, but not using public library
def hex_to_bin_unit(hex_unit):
    hex_unit = str(hex_unit)
    if hex_unit == 'A':
        dec_num = 10
    elif hex_unit == 'B':
        dec_num = 11
    elif hex_unit == 'C':
        dec_num = 12
    elif hex_unit == 'D':
        dec_num = 13
    elif hex_unit == 'E':
        dec_num = 14
    elif hex_unit == 'F':
        dec_num = 15
    else:
        dec_num = int(hex_unit)
    
    dummy = dec_num
    bin_storage = ''
    while dummy >=2:
        remainder = dummy % 2
        bin_storage += str(remainder)
        dummy = dummy // 2
    
    bin_storage += '1'

    bin_form = bin_storage[::-1]

    if len(bin_form) !=4:
        bin_form = (4-len(bin_form)) * '0' + bin_form
    
    return bin_form, dec_num

def hex_to_bin_dec(hex_number):
    max_power = len(hex_number) - 1
    dec_form = 0
    bin_form = ''
    for i in str(hex_number):
        bin_num, dec_num = hex_to_bin_unit(i)
        dec_form += dec_num * 16**max_power
        max_power -= 1
        bin_form += bin_num
    
    print(f"The decimal form of {hex_number} (hex): {dec_form}")
    print(f"The binary form of {hex_number} (hex): {bin_form}")

hex_to_bin_dec('DA3')
'''Output
The decimal form of DA3 (hex): 3491
The binary form of DA3 (hex): 110110100011
'''
