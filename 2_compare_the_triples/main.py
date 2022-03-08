def compareTriplets(a, b):
  i = 0
  result = [0, 0]
  while i < 3:
    if a[i] > b[i]:
      result[0] += 1
    elif a[i] < b[i]:
      result[1] += 1
    i += 1
  return result
  

a1 = [5, 6, 7]
b1 = [3, 6, 10]

a2 = [17, 28, 30]
b2 = [99, 16, 8]

a3 = [1,2,3]
b3 = [1,2,3]

x = compareTriplets(a3, b3)
print(x)