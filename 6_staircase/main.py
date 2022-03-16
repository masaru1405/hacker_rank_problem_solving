def staircase(n):
  i = 1
  while i <= n:
    spaces = n - i
    print("{}{}".format((" " * spaces), ("#" * i)))
    i += 1


staircase(6)
