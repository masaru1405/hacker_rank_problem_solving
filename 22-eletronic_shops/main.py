def getMoneySpent(keyboards, drives, b):
  value = -1
  for i in keyboards:
    for j in drives:
      temp = i + j
      if temp <= b and temp > value:
        value = temp
  return value


b = 5
k = [4]
d = [5]
resp = getMoneySpent(k, d, b)
print(resp)