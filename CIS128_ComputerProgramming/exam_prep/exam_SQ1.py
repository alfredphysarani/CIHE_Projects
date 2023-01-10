height_cm = float(input("Please input the height of a person in the unit of cm: "))

def round_up_two_decimal(num):
    # as per the requirement: the number of inches is a floating-point number rounded up to 2 decimal points. 
    if num*1000 % 10 == 0:
        return num
    else:
        dum = num*1000//10+1
        return dum/100

def cm_to_inch(h):
    return h / 2.54

def inch_to_feet(inch):
    feet = inch // 12
    remainder = inch % 12
    return feet, round_up_two_decimal(remainder)

height_inch = cm_to_inch(height_cm)
height_feet, height_r_inch = inch_to_feet(height_inch)

print(f"The height of the person in feet and inches: {int(height_feet)} ft, {height_r_inch} in")