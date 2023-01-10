print("Median in 3 numbers finder")
num_line =input("Please input several numbers and use space to separate the numbers (Example: 1 3.3):")

num_str_list = num_line.split()
num_list = []

for n in num_str_list:
    num_list.append(float(n))

def num_arranger(num_list):
    result_list = []
    min_n = float(num_list[0])
    max_n = float(num_list[0])
    for num in num_list:
        if float(num) <= min_n:
            min_n = num
        if float(num) >= max_n:
            max_n = float(num)
    
    dummy_list = num_list.copy()
    dummy_list.remove(min_n)
    dummy_list.remove(max_n)

    result_list.append(min_n)
    result_list.append(dummy_list[0])
    result_list.append(max_n)

    return result_list

print(f"The median is {num_arranger(num_list)[1]}")