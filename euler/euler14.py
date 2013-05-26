from func import iseven

done = {}
seq = lambda num: num / 2 if iseven(num) else 3 * num + 1

for value in range(2, 1000001):

    ini_val = value
    terms = 1

    while value != 1:

        value = seq(value)
        terms += 1

        if value in done and value != 1:
            terms += done[value] - 1
            value = 1

    done[ini_val] = terms

key, value = max(done.iteritems(), key=lambda x: x[1])

print 'Result = %s (%s)' % (key, value)
print 'Result = 837799 (525)'
