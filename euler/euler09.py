import math

for a in range(1, 1000):
    for b in range(1, 1000):

        if a < b:
            c = math.sqrt(a ** 2 + b ** 2)
            value = a + b + c

            if value == 1000:
                print 'a = %s, b = %s, c = %s, a*b*c =  %s' % (a, b, c, a * b * c)
                break


print 'a = 200, b = 375, c = 425.0, a*b*c =  31875000.0'