from fractions import gcd

def permToCycles(perm):
    pi = {i+1: perm[i] for i in range(len(perm))}
    cycles = []

    while pi:
        elem0 = next(iter(pi))
        this_elem = pi[elem0]
        next_item = pi[this_elem]

        cycle = []
        while True:
            cycle.append(this_elem)
            del pi[this_elem]
            this_elem = next_item
            if next_item in pi:
                next_item = pi[next_item]
            else:
                break
        

        cycles.append(cycle)

    return cycles

#no need
'''def findOrbits(perm):
    pi = {i+1: perm[i] for i in range(len(perm))}
    cycles = []

    while pi:
        elem0 = next(iter(pi))
        this_elem = pi[elem0]
        next_item = pi[this_elem]

        cycle = []
        while True:
            cycle.append(this_elem)
            del pi[this_elem]
            this_elem = next_item
            if next_item in pi:
                next_item = pi[next_item]
            else:
                break
        cycle.sort()
        
        cycles.append(cycle)

    return cycles'''

def findGCD(lengths):
	res = gcd(*lengths[:2])
	for length in lengths[2:]:
		res = gcd(res, length)
	return res

def findLCM(lengths):
	mul = 1
	for length in lengths:
		mul *= length
	return mul/findGCD(lengths)

def findOrder(cycles):
	lengths = []
	for cycle in cycles:
		lengths.append(len(cycle))
	return findLCM(lengths)



def permutationInput(n):
	perm = raw_input("Give me Sn (n numbers with space in between): ")
	perm = perm.split(" ")
	plhthos = []
	perm = map(int, perm)
	if len(perm) != n:
		print "Wrong! Give me n numbers: "
		perm = raw_input("Give me Sn (n numbers with space in between): ")
		perm.split(" ")
		for number in perm:
			try:	
				number = int(number)
			except ValueError:
				print "Give me integers! "
	for i in xrange(1,n+1):
		plhthos.append(i)
	return perm,plhthos

def inversePerm(perm):
	invperm = []
	for i in range(len(perm)):
		invperm.append(0)
	for element in perm:
		invperm[element - 1] = perm.index(element) + 1
	return invperm

def permToTranspositions(cycles):
	transprod = []
	for cycle in cycles:
		transpose = []
		for num in cycle[len(cycle)-1:0:-1]:
			tupla = cycle[0],num
			transpose.append(tupla)
		transprod.append(transpose)
	return transprod

def main():
	n = int(raw_input("Give me [n]: "))
	permtuple = permutationInput(n)
	permlist = permtuple[0]
	plhthos = permtuple[1]
	cycles = permToCycles(permlist)
	#orbits = findOrbits(permlist)
	length = n
	transpositions = []
	p = 0
	for num in permlist:
		for i in xrange(permlist.index(num)+1,len(permlist)):
			if num > permlist[i]:
				p += 1
	print "Length of Sn:"
	print length
	print "Inverse Sn: "
	print inversePerm(permlist)
	print "Sn as a product of disjoint cycles: "
	for cycle in cycles:
		print "("+''.join(str(e) for e in cycle)+")",
	print ""
	print "Number of Paraviaseis: ",p
	print "Sn as a product of transpositions: "
	for pinakakiklou in permToTranspositions(cycles):
		for antimetathesi in pinakakiklou:
			transpositions.append(antimetathesi)
			print antimetathesi,
	print ""
	if len(transpositions) % 2 == 0:
		print "Permutation is EVEN"
	else:
		print "Permutation is ODD"
	print "Order is: ",findOrder(cycles)

if __name__ == "__main__":
	main()	



