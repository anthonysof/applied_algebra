import sys

def matrixMultiplier(p, n):
	m = [[0 for x in range(n)] for x in range(n)]

	for i in range(1,n):
		m[i][i] = 0;

	for L in range (2,n):
		for i in range(1,n-L+1):
			j = i+L-1;
			m[i][j] = sys.maxint

			for k in range(i,j):
				q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j];
				if q < m[i][j]:
					m[i][j] = q
	return m[1][n-1]

def main():
	#n = int(raw_input("Enter number of matrices: "))
	n = 5
	print("Number of matrices: "+str(n))
	

	arr = []
	print("Give me dimensions")
	for i in range(0,n*2):
		arr.append(int(raw_input("Give me d"+str(i/2)+": ")))
		while(i>1 and i%2==0 and arr[i-1]!=arr[i]):
			print "Wrong dimensions for matrix multiplication, try again"
			arr[i] = int(raw_input("Give me d"+str(i/2)+": "))


	res = matrixMultiplier(arr, len(arr))
	print("Minimum number of multiplications is: "+str(res))





if __name__ == "__main__":
	main()	