
# forum

def check(num):
    for i in range(11, 20):
        if num % i != 0:
            return False
    return True


num = 11*12
fac = 11*12

var = False
while var == False:
    print num
    var = check(num)
    num += fac


