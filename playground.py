import re

name = 'Neymar Middle Middle Jr'

print("Jr." in name)

pattern = re.compile("^[A-Z][a-z]+\s([A-Z][a-z]+\s)+[A-Z][a-z]$")

check = re.fullmatch(pattern, name)
print(check)

check = re.search(pattern, name)
print(check)

print(int(13.9999999999999))

print(13.9999%1)

print(1.2525//1)
print(1.7//1)
print(1.999999//1)
print(0.99999//1)
print(-0.1//1)