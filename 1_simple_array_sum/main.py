def simpleArraySum(ar):
	sum = 0
	for i in ar:
		sum += i
	return sum


arr1 = [1,2,3,4,5]
resp = simpleArraySum(arr1)
print(resp)