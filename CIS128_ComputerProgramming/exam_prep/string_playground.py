'''
String Library
'''

# Escaping Characters (\)
print("Quote: \"")
print("Tab: \ttxt")
print("Newline: \n")
print("backslash: \\")

# in for syntax
print("a0" in "1a0c")
print("ac" in "1a0c")

# Indexing
color = "yellow"    # 0:y 1:e 2:l 3:l 4:o 5:w
print(color[1])     # -> "e"
print(color[-1])    # -> "w"
print(color[4:5])   # -> "o"
print(color[4:6])   # -> "ow"
print(color[:4])    # -> "yell"
print(color[:4:2])  # -> "yl"
print(color[-3:])   # -> "low"
print(color[3:])    # -> "low"
print(color[-3::-1]) # -> "lley"

# length of string
print(len("hello"))

# .format()
print("A bird is {} and {}".format("eating", "flying"))
print("A bird is {action1} and \
    {action2}".format(action2="eating", action1="flying"))

# .lower() and .upper
print("abc123".upper())
print("ABC123".lower())

# .strip() only the beginning and ending chars affected
text_1 = ' ... lemon + ... - '
print(text_1.strip())
print(text_1.strip(" ."))
print(text_1.strip(". "))
print(text_1.strip(".+ "))
print(text_1.strip("-. "))

# .title() capitalize
var = "lydia's days"
print(var.title())

# .split() split chars into list
text = "Silicom Valley"
print(text.split())
print(text.split('l'))

# .find() find whether a char is in the string
mountain_name = "Mount Fuji"
print(mountain_name.find("o"))  # 1
print(mountain_name.find("c"))  # -1
print(mountain_name.find("ot")) # -1
print(mountain_name.find("ou")) # 1

# .replace() characters
fruit = "apple"
print(fruit.replace("p", "P ")) # aP P le

# .join() 
print(".".join(["www", "google", "com"]))

# .isalpha(), .isnumeric(), .isalnum()
print("abc".isalpha())      # True
print("abc1".isalpha())     # False
print("abc ".isalpha())     # False
print("123".isnumeric())    # True
print("12.3".isnumeric())   # False
print("abc1".isalnum())     # True