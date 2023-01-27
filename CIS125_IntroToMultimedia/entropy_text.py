'''
To calculate the entropy of string
'''
from math import log2

message = "aaaaaaaabbbbccde"
# message = "aaaaabbbbbabbabbbababbbabbbabababbaaaaabbabbba"
# message = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
sym_dict = {}

# frequency distribution
for symbol in message:
    if symbol not in sym_dict:
        sym_dict[symbol] = {}
        sym_dict[symbol]["Freq"] = 1
    else:
        sym_dict[symbol]["Freq"] += 1

print(f"There are {len(sym_dict.keys())} unique symbols.")
print(sym_dict.keys())
print(f"Frequency Dist of Symbols: {sym_dict}")

# Probability
for symbol in sym_dict:
    sym_dict[symbol]["Prob"] = sym_dict[symbol]["Freq"]/len(message)

# Self-Info
for symbol in sym_dict:
    sym_dict[symbol]["Self-Info"] = log2(1/sym_dict[symbol]["Prob"])

H = 0
# Entropy
for symbol in sym_dict:
    H += sym_dict[symbol]["Prob"] * sym_dict[symbol]["Self-Info"]

print(sym_dict)
print("Entropy: " + str(H))


