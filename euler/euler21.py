# Solved - 31626
from func import amicable

result = []
for num in range(1, 10001):
    if amicable(num) and num not in result:
        result.append(num)

print sum(result)
