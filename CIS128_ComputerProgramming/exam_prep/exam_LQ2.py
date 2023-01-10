print("Min, Max and Mean Calculator")

num_line =input("Please input several numbers and use space to separate the numbers:")
print(num_line)

num_str_list = num_line.split()
num_list = []

for n in num_str_list:
    num_list.append(float(n))

def min_max_calc(num_list):
    min_n = float(num_list[0])
    max_n = float(num_list[0])
    for num in num_list:
        if float(num) <= min_n:
            min_n = num
        if float(num) >= max_n:
            max_n = float(num)
    
    return min_n, max_n

min_result, max_result = min_max_calc(num_list)
print(f"Min: {min_result}")
print(f"Max: {max_result}")
print(f"Mean: {sum(num_list)/len(num_list)}")
