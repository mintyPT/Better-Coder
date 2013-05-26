from func import isprime

_sum = sum([i for i in range(2, 2000001) if isprime(i)])

print _sum
print '142913828922'
