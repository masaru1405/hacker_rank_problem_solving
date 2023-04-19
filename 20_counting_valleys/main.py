def countingValleys(steps, path):
  lista = []
  for i in path:
    if i == 'U':
      lista.append(1)
    else:
      lista.append(-1)
  
  j = 0
  hike = 0
  count_valleys = 0
  while j < n:
    hike += lista[j]
    if hike == 0:
      count_valleys += 1
    j += 1

[1,-1,-1,-1,1,-1,1,1]
resp = countingValleys(0, 'UDDDUDUU')
print(resp)