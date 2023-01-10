print("nCr calculator")
n = int(input("Please type in an integer for n: "))
r = int(input("Please type in an integer for r: "))

def factorial(num: int):
    if num == 1 or num == 0:
        return 1
    return factorial(num-1)*num

def nCr(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))

print(int(nCr(n,r)))
