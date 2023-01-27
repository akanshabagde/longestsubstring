def LCSubStr(X, Y, m, n):

	LCS= [[0 for k in range(n+1)] for l in range(m+1)]

	result = 0

	for i in range(m + 1):
		for j in range(n + 1):
			if (i == 0 or j == 0):
				LCS[i][j] = 0
			elif (X[i-1] == Y[j-1]):
				LCS[i][j] = LCS[i-1][j-1] + 1
				result = max(result, LCS[i][j])
			else:
				LCS[i][j] = 0
	return result



X = 'I am learning Python'
Y = 'It is easy to use'

m = len(X)
n = len(Y)

print('Length of Longest Common Substring is',
	LCSubStr(X, Y, m, n))

