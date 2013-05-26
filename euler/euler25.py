from func import fibo

def Digits(num):
    myStr = str(num)
    return myStr.__len__()


fiboArray = [1, 1]

print len(fiboArray), fiboArray[-2]
print len(fiboArray), fiboArray[-1]


while Digits(fiboArray[-1]) < 1000:
    num1 = fiboArray[-2]
    num2 = fiboArray[-1]

    fiboArray.append(fibo(num1, num2))

    print len(fiboArray), fiboArray[-1]