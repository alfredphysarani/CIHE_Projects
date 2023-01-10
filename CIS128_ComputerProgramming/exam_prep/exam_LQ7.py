input_list = eval(input("Please input a list of characters (Example: [1, 2, 3, 'b', 'c']): "))

output = ''
for item in input_list:
    output += str(item)

print(output)
