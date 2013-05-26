from func import factorial

mult = factorial(100)

_sum = [int(str(mult)[i]) for i in range(len(str(mult)))]
_sum = sum(_sum)


print _sum
print '648'