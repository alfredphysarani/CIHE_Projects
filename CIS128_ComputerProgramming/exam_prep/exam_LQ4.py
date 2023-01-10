n_list = eval(input("Please input a list of integer (Example: [1, 2, 3, 5, 4]): "))

count = 0
for i in n_list:
    if float(i) == 4.0:
        count += 1
        
print(f"The count of 4 in the list: {count}")