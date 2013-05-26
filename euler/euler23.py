import lib

def numberType(num):
	_p = lib.d(num)
	# Deficient number
	if _p < num:
		return 0 
	# Perfect number
	elif _p == num:
		return 1
	# Abundant number
	else: 
		return 2


maxim = 1000


ab = [num for num in range(1, maxim) if numberType(num) == 1]

print ab
# ab = [num for num in range(1, maxim) if numberType(num) == 2]
sumab = lib.allSums(ab)
 
print sumab

# invab = []
# for i in range(max(sumab)):
# 	if i not in sumab:
# 		invab.append(i)
# print invab
# print sum(invab)

# print len(ab), ab
# print sumab
