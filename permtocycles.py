def permToCycles(perm):
    pi = {i+1: perm[i] for i in range(len(perm))}
    cycles = []

    while pi:
        elem0 = next(iter(pi)) # arbitrary starting element
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

def permutationInput():
	n = int(raw_input("Give me [n]: "))
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
		print element - 1
		invperm[element - 1] = perm.index(element) + 1
	return invperm

def main():
	permtuple = permutationInput()
	permlist = permtuple[0]
	plhthos = permtuple[1]
	cycles = permToCycles(permlist)
	print cycles
	print inversePerm(permlist)


if __name__ == "__main__":
	main()	



