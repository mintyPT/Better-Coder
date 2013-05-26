# solved
def powerSum(_num, _pow):
	sum = 0
	for n in str(_num):
		sum += int(n)**_pow
	return sum

def check(_num, _pow):
	if _num == powerSum(_num, _pow):
		return True
	else:
		return False

vec = [_n for _n in range(2, 1000000) if check(_n, 5)]

print vec, '==>',sum(vec)
	