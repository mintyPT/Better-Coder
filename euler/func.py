import math


def factorial(n):
    '''Return the factorial of n'''
    total = 1
    while n!=1:
        total = total * n
        n-=1
    return total


def lastTen(num):
    '''Return the last 10 numbers os num'''
    myStr = str(num)
    myStr = myStr[-10:]
    return int(myStr)


def factor(n):
    '''Return the factors of n'''
    factors = []
    f = 1
    limit = math.sqrt(n) + 1
    while f <= limit:
        if n % f == 0:
            factors.append(f)
            factors.append(n / f)
        f = f + 1

    factors.sort()

    facts = []

    for num in factors:
        if isprime(num) == True:
            facts.append(num)

    print max(facts)


def isprime(x):
    '''Return True if x is a prime number'''
    x = abs(int(x))
    if x < 2:
        return "Less 2", False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        for n in range(3, int(x ** 0.5) + 2, 2):
            if x % n == 0:
                return n, False
        return True


def ispalindrome(num):
    '''Return True is number num is a palindrome'''
    strnum = str(num)
    strnumI = strnum[::-1]

    if strnum == strnumI:
        return True
    else:
        return False


def ismultiple(num, multiple):
    '''Return True is num is a multiple of multiple'''
    if num % multiple == 0:
        return True
    else:
        return False


def fibo(num1, num2):
    '''To be used to generate fibonacci sequences'''
    return num1 + num2


def iseven(num):
    '''Return True is num is even'''
    if num % 2 == 0:
        return True
    else:
        return False


def properDivisors(_n):
    '''Find the proper divisor of a number'''
    return [i for i in range(_n / 2, 0, -1) if _n % i == 0]


def d(num):
    '''Sum of the proper divisors'''
    return sum(properDivisors(num))


def amicable(num):
    '''Verify if a number is amicale'''
    return num == d(d(num)) and num != d(num)


def allSums(vec):
    '''Calculate all the possible sums between the numbers of a vector'''
    import itertools
    r = [i + j for i, j in list(itertools.combinations_with_replacement(vec, 2))]

    s = []
    for v in r:
        if v not in s:
            s.append(v)
    return s
