num = str(2 ** 1000)

_sum = sum([int(num[i]) for i in range(len(num))])

print _sum
print _sum == 1366
