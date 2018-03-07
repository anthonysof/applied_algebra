from fractions import gcd

def findLCM(tupla):
	a = tupla[0]
	b = tupla[1]
	return a*b/gcd(a,b)

def main():
	n = int(raw_input("Dose mou n: "))
	sums = []
	for i in xrange(1,n+1):
		for j in xrange(1,n+1):
			if i+j == n:
				tupla = i,j
				sums.append(tupla)
	print sums
	LCMs = []
	for tupla in sums:
		LCMs.append(findLCM(tupla))
	print "Maximum possible order of S"+str(n)+" which is a product of 2 disjoint cycles with lengths k1+k2 = "+str(n)+" is: "
	print max(LCMs)

if __name__ == "__main__":
	main()	