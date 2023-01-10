dig = 9

# decimal to binary
print(bin(dig))

# decimal to hex
print(hex(dig))

# bin to decimal
print(int(bin(dig), 2))

# heximal to decimal
print(int(hex(dig), 16))

'''
Negative number presentation:
Method 1: Sign & Mangnitude
    Computer memory
        1-bit for sign
        7-bit for magnitude
        Example: 
            0001001 = 9
            10001001 = -9

Method 2:
    1. Find the positive binary value for a negative number
    2. Add a 0 to the front of the number
    3. Invert each bit of the number
    4. Add 1 to the number

    Example: Finding the binary form of -9
        1. 0001001 = 9
        2. 00001001
        3. Inverted becomes 11110110
        4. 11110111 = (-128 + 64 + 32 + 16 + 4 + 2 + 1)
'''

result = -128 + 64 + 32 + 16 + 4 + 2 + 1
print(result)