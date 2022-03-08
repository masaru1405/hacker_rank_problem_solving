def diagonalDifference(arr):
	left_diagonal = 0
	right_diagonal = 0
	index_last_col = len(arr[0]) - 1
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			if i == j:
				left_diagonal += arr[i][j]
		right_diagonal += arr[i][abs(i-index_last_col)]
	return abs(left_diagonal - right_diagonal)


m1 = [[1,2,3], [4,5,6], [9,8,9]]
m2 = [[11,2,4], [4,5,6], [10,8,-12]]
resp = diagonalDifference(m2)
print(resp)
