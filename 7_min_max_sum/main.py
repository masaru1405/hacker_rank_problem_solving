def insertionSort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i -1
    while j >= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key
  return arr

def miniMaxSum(arr):
  array = insertionSort(arr)
  min_value = array[0]
  max_value = array[-1]
  temp = 0 
  for i in array:
    temp += i
  sum_min = temp - max_value
  sum_max = temp - min_value
  print("{} {}".format(sum_min, sum_max))

array = [1, 2, 3, 4, 5]
array2 = [7, 69, 2, 221, 8974]
resp = miniMaxSum(array2)
