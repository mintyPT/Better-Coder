
from func import ispalindrome

palins = []

for i in range(999,1,-1):
    for j in range(999,1,-1):
        mul = i * j
        if ispalindrome(mul):
            palins.append(mul)

print max(palins)

