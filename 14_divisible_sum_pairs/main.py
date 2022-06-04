def divisibleSumPairs(n, k, ar):
	max_index = n - 1 #n é a quantidade de items
	i = 0
	resp = 0
	while i < max_index:
		j =  i + 1
		while j <= max_index: 
			if((ar[i] + ar[j]) % k == 0):
				resp += 1
			j += 1
		i += 1
	
	return resp


n = 6
k = 3
lista = [1, 3, 2, 6, 1, 2]

r = divisibleSumPairs(n, k, lista)
print(r)