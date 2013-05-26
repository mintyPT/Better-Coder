from func import lastTen

pim = 1
exp = 7830457

while exp > 0:
    if exp > 200:
        fac = 200
        exp -= 200
    else:
        fac = exp
        exp = 0

    two = 2 ** fac
    two = lastTen(two)
    pim = lastTen(pim * two)

um = 28433 * pim + 1

print lastTen(um)
print lastTen(um) == 8739992577
