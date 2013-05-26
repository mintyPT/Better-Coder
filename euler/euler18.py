from pprint import pprint
import array


def solve(str):

    numbers = []

    i = 0
    for line in str.split('\n'):
        tempLine = []
        for num in line.split(' '):
            if num != '':
                num = int(num)
                tempLine.append(num)
            #numbers[i].append(num)
        #print tempLine
        if tempLine.__len__() != 0:
            numbers.insert(i, tempLine)
        i += 1

    for line in range(len(numbers)-2,-1,-1):
    #    print line

        ind = 0
        for num in numbers[line]:
            num1 = num + numbers[line+1][ind]
            num2 = num + numbers[line+1][ind+1]

            if num1>num2:
                maxNum = num1
            else:
                maxNum = num2

            numbers[line][ind] = maxNum

            ind += 1


    return int(numbers[0][0])











str = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


print solve(str)

url = 'http://projecteuler.net/project/triangle.txt'

import urllib

f = urllib.urlopen(url)
str = f.read()
print solve(str)