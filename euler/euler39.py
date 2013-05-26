import math

def isinteger(num):
    if num - round(num) == 0:
        return True
    else:
        return False

def cf(a, b):
    c = math.sqrt(a**2 + b**2)
    return c
def perimeter(a, b, c):
    return a+b+c

def sortAndUniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  output.sort()
  return output


pval = []

for a in range(1, 3000):
    for b in range(1, 3000):

        c = math.sqrt(a**2 + b**2)

        if isinteger(c):
            p = a + b + c
            if p <= 1000 and isinteger(p)==True:
                pval.append(p)
            


            

vals = sortAndUniq(pval)
print vals

occMaster = 0
pMaster = 0
for i in range(len(vals)):
    occ = 0;
    teste = vals[i]

    for j in range(len(pval)):
        if pval[j]==teste:
            occ += 1


    if occ>occMaster:
        occMaster = occ
        pMaster = teste

print occMaster, pMaster