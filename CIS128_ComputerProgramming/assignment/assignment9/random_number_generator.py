import random

with open('Random_number.txt', 'w', encoding='utf-8') as f:
    for i in range(0, 1000):
        f.write(str(random.randint(1,1000)) + "\n")
    