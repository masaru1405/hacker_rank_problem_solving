def plusMinus(arr):
  size = len(arr)
  positive = 0
  negative = 0
  zero = 0
  for i in arr:
    if i > 0:
      positive += 1
    elif i < 0:
      negative += 1
    else:
      zero += 1
  
  ratio_positive = positive / size
  ratio_negative = negative / size
  ratio_zero = zero / size
  print("{:.6f}".format(ratio_positive))
  print("{:.6f}".format(ratio_negative))
  print("{:.6f}".format(ratio_zero))


arr1 = [1,1,0,-1,-1]
arr2 = [-4,3,-9,0,4,1]
arr3 = [0, 100, 35, 0, 94, 40, 42, 87, 59, 0]
plusMinus(arr3) 