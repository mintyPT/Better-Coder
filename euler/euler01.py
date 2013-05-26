from func import ismultiple


l = [i for i in range(1, 1000) if ismultiple(i, 3) or ismultiple(i, 5)]
res = sum(l)

print res
print res == 233168
