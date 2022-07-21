def bonAppetit(bill, k, b):
  sum_items = 0
  for i in bill:
    sum_items += i
  cost_per_person = int(sum_items / 2)
  print(cost_per_person)

  sum_items_anna = 0
  bill_anna = bill[:]
  del bill_anna[k]
  for j in bill_anna:
    sum_items_anna += j
  cost_anna = int(sum_items_anna / 2)
  print(cost_anna)

  if(cost_anna == b):
    print('Bon Appetit')
  else:
    diff = b - cost_anna
    print(diff)

#Test
x = [72, 53, 60, 66, 90, 62, 12, 31, 36, 94]
bonAppetit(x, 6, 288)
