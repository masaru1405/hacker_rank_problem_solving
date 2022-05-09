def breakingRecords(scores):
  min_score = scores[0]
  max_score = scores[0]
  count_min = 0
  count_max = 0

  for score in scores:
    if score < min_score:
      min_score = score
      count_min += 1
    if score > max_score:
      max_score = score
      count_max += 1
  
  return [count_max, count_min]

#Teste
scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
scores2 = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
resp = breakingRecords(scores2)
print(resp)
