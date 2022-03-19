def birthdayCakeCandles(candles):
  max_height = 0
  count = 0 
  for i in candles:
    if i > max_height:
      max_height = i
  for i in candles:
    if i == max_height:
      count += 1
  return count

array = [44, 53, 31, 27, 77, 60, 66, 77, 26, 36]
array2 = [18, 90, 90, 13, 90, 75, 90, 8, 90, 43]
resp = birthdayCakeCandles(array)
print(resp)