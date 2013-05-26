from func import isprime


primes, size, i = [], 0, 2

while len(primes) < 10001:
    if isprime(i) == True:
        primes.append(i)
    i += 1


print primes
print len(primes)
print '10001'
