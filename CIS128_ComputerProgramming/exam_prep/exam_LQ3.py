n = int(input("Please input an integer: "))

for i in range(1, n+1):
    print("*"*i)

for i in range(1, n):
    print("*"*(n-i))