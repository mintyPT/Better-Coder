# Solved
import math

def checkPalindrome(_num):
	_s = str(_num)
	_l = int(math.floor(len(_s)/2.0))

	for i in range(_l):
		if _s[i] != _s[-(1+i)]:
			return False
	return True

def toBin(_num):
	return bin(_num)[2:].rjust(0, '0')

result = [_num for _num in range(0, 1000001) if checkPalindrome(_num) and checkPalindrome(toBin(_num))]
print result, sum(result)
	