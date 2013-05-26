import math
import random
from pprint import pprint


def toss():
    '''Toss a coin'''
    return round(random.random())


results = []

for p in range(1,21):

    CAPITAL = 1.0

    PROPORTION = 1/p

    for i in range(1000):


        CAP = CAPITAL * (1.0 - PROPORTION)
        BAT = CAPITAL * PROPORTION * 2.0 * toss()

        CAPITAL = CAP + BAT

        print CAPITAL, PROPORTION

        if CAPITAL < 0.01:
            break

    results.append([CAPITAL, PROPORTION])

# pprint(results)
