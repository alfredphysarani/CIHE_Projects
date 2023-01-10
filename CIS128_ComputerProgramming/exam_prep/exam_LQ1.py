print("palindrome checker")
input_str = input("Please input a string:")

def palindrome_checker(input_str: str):
    if len(input_str) <= 1:
        return True
    
    return input_str[0] == input_str[-1] and palindrome_checker(input_str[1:-1])

if palindrome_checker(input_str):
    print("Yes, it is a palindrome.")
else:
    print("No, it is not a palindrome.")