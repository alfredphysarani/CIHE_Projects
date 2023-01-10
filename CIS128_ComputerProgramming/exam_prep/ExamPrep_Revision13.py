'''
Revision 13
'''

'''
Exercise 1
How to directly input a list?
How to directly input a tuple?
'''

'''
a = eval(input())
print(a)
print(type(a))
'''

'''
Exercise 2
Write a Python program to get the smallest number from a list.
'''

def smallest_finder(num_list):
    smallest = num_list[0]
    for i in num_list:
        if i <= smallest:
            smallest = i
    
    return smallest

print(smallest_finder([4,5,4,2]))

'''
Exercise 3
Write a Python program to remove duplicates from a list.
'''

def remove_dup(in_list):
    unique_list = []
    for item in in_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

print(remove_dup([10, 20, 30, 20, 10, 50, 60, 20, 20]))

'''
Exercise 4
Write a Python program to split a list every Nth element.
'''
def list_spliter(in_list, n):
    result_list = []
    for i in range(0, n):
        dum_list = []
        for j in range(0, len(in_list)//n+1):
            if i + n*j < len(in_list):
                dum_list.append(in_list[i + n*j])
        
        result_list.append(dum_list)
    
    return result_list

print(list_spliter(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 3))

# simplier solution
def list_silce(in_list, step):
    return [in_list[i::step] for i in range(step)]

'''
Exercise 5
Write a Python program that converts a given string list to a tuple.
'''
def string_to_tuple(in_str):
    return tuple(x for x in in_str if not x.isspace())
    

print(string_to_tuple('python 3.0'))

'''
Exercise 6
Write a Python program to compute the element-wise sum of 
given tuples
'''
tup_1 = (1,2,3,4)
tup_2 = (3,5,2,1)
tup_3 = (2,2,3,1)
print(sum(tup_1))
result = []

for i in range(0, len(tup_1)):
    result.append(tup_1[i] + tup_2[i] + tup_3[i])

print(tuple(result))

# OR
print(tuple(map(sum, zip(tup_1, tup_2, tup_3))))


