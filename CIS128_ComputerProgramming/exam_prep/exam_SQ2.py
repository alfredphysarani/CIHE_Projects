start=float(input("Please input an integer for the start: "))
end=float(input("Please input an integer for the end (greater than the start integer): "))

# adaption to float also
def round_up_int(num):
    # as per the requirement: the number of inches is a floating-point number rounded up to 2 decimal points. 
    if num*10 % 10 == 0:
        return int(num)
    else:
        dum = num*10//10+1
        return int(dum)

print(round_up_int(start), round_up_int(end))

for i in range(round_up_int(start), round_up_int(end)):
    if i%2==1:
        print(i)

