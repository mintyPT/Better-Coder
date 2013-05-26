
import math

def pentagonal(n):
    n = float(n)
    fac1 = n/2
    fac2 = (3*n) - 1

    return fac1 * fac2

def pent2n(pent):

    a = 3
    b = -1
    c = -2 * pent

    valp = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    valn = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

    return valp, valn

def isinteger(num):
    if num - round(num) == 0:
        return True
    else:
        return False

def ispentagonal(val):
    num = pent2n(val)[0]
    if isinteger(num) == True:
        return True
    else:
        return False




def genpentags(amount):
    pentags = []
    i = 1
    while len(pentags)<amount:
        pentags.append(pentagonal(i))
        i += 1
    return pentags


pentags = genpentags(10000)

print 'starting mixing values'

for i in range(len(pentags)):
    for j in range(len(pentags)):

        sum = pentags[i] + pentags[j]
        dif = pentags[i] - pentags[j]
        dif = abs(dif)

        #if ispentagonal(sum)==True:
        #    print 'sum,', pentags[i], pentags[j], sum

        #if ispentagonal(dif)==True:
        #    print 'dif,', pentags[i], pentags[j], dif

        if (ispentagonal(sum)==True) and (ispentagonal(dif)==True):
            print '-------- found it!', pentags[i], pentags[j], sum, dif

