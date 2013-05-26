import urllib

dic = {'a': 1,
       'b': 2,
       'c': 3,
       'd': 4,
       'e': 5,
       'f': 6,
       'g': 7,
       'h': 8,
       'i': 9,
       'j': 10,
       'k': 11,
       'l': 12,
       'm': 13,
       'n': 14,
       'o': 15,
       'p': 16,
       'q': 17,
       'r': 18,
       's': 19,
       't': 20,
       'u': 21,
       'v': 22,
       'w': 23,
       'x': 24,
       'y': 25,
       'z': 26}

url = 'http://projecteuler.net/project/names.txt'

uh = urllib.urlopen(url)
source = uh.read()

source = str(source)
source = source.replace('\"', '')


list = str(source).split(',')
list = sorted(list)



def score(name):
    scoreV = 0
    for i in range(len(name)):
        letter = name[i]
        letter = str(letter)
        letter = letter.lower()

        for key in dic:
            if letter == key:
                scoreV += dic[key]
    return scoreV



total = 0
for v in range(len(list)):
    total += score(list[v]) * (v+1)

print(total)