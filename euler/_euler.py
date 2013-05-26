

# ===================================================

# Solved
def e29():
	vec = []
	for a in range(2, 101):
		for b in range(2, 101):
			result = a**b
			if result not in vec:
				vec.append(result)
	print len(vec)



def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def getFromUrl(url):
    import urllib
    f = urllib.urlopen(url)
    content = f.read()
    f.close()
    return content


def readMessage59(vec):
	s = []
	for v in vec:
		s.append(chr(v))
	return ''.join(s)

# Solved
def e59():
	url = 'http://projecteuler.net/project/cipher1.txt'
	data = getFromUrl(url).replace('\n','').replace('\r','').split(',')
	data = [int(d) for d in data]

	import operator

	for p1 in range(97, 123):
		for p2 in range(97, 123):
			for p3 in range(97, 123):

				password = [p1, p2, p3]
				f = []
				for l in list(chunks(data, 3)):
					if(len(l) == 3):
						f.append(operator.xor(l[0], password[0]))
						f.append(operator.xor(l[1], password[1]))
						f.append(operator.xor(l[2], password[2]))
					else:
						f.append(operator.xor(l[0], password[0]))

				ok = 0;
				out = 0;
				for number in f:
					if (number >= 97 and number <= 122) or (number >= 65 and number <= 90):
						ok +=1
					else:
						out +=1

				perc = ok * 100.0 / (ok + out)

				original_text = ''
				if perc > 76.0:
					print 'passord: %d %d %d, letra = %d, outra = %d ==> %f' % (password[0], password[1], password[2], ok, out, perc)
					original_text =  readMessage59(f)

					s = 0
					for c in original_text:
						s += ord(c)

					print s

					return







if __name__ == '__main__':
	e59()
