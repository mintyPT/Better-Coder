target = 100

sum1, sum2 = 0, 0

for i in range(1, target + 1):
    sum1 += i ** 2
    sum2 += i

sum2 = sum2 ** 2

print sum1, sum2, sum2 - sum1
print '338350 25502500 25164150'
