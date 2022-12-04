num = 492357816

sum_row1 = int(str(num)[0]) + int(str(num)[1]) + int(str(num)[2])
sum_row2 = int(str(num)[3]) + int(str(num)[4]) + int(str(num)[5])
sum_row3 = int(str(num)[6]) + int(str(num)[7]) + int(str(num)[8])

sum_col1 = int(str(num)[0]) + int(str(num)[3]) + int(str(num)[6])
sum_col2 = int(str(num)[1]) + int(str(num)[4]) + int(str(num)[7])
sum_col3 = int(str(num)[2]) + int(str(num)[5]) + int(str(num)[8])

sum_diag1 = int(str(num)[0]) + int(str(num)[4]) + int(str(num)[8])
sum_diag2 = int(str(num)[2]) + int(str(num)[4]) + int(str(num)[6])

print(sum_row1, sum_row2, sum_row3, sum_col1, sum_col2, sum_col3, sum_diag1, sum_diag2)


print(str(12.3).isnumeric())