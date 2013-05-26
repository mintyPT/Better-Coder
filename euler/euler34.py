# solved
def fac(n):
	if n == 1:
		return 1
	else:
		return n * fac(n-1)

def fac2(_num):
	res = 1
 	for i in range(_num, 1, -1):
 		res *= i
 	return res


def facSum(_num):
	sum = 0
	for n in str(_num):
		sum += fac2(int(n))
	return sum


def check(_num):
	if _num == facSum(_num):
		return True
	else:
		return False

vec = [_n for _n in range(3, 200000) if check(_n)]
print vec, '==>',sum(vec)



