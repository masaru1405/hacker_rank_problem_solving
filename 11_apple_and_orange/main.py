def countApplesAndOranges(s, t, a, b, apples, oranges):
  count_apples = 0
  count_oranges = 0
  for i in apples:
    apple_dist = a + i
    if s <= apple_dist <= t:
      count_apples += 1
  for j in oranges:
    orange_dist = b  j
    if s <= orange_dist <= t:
      count_oranges += 1
  print("{}\n{}".format(count_apples, count_oranges))