
def catAndMouse(x, y, z):
  a = z-x
  if a < 0:
    a *= -1

  b = z-y
  if b < 0:
    b *= -1

  if a < b:
    return 'Cat A'
  elif b < a:
    return 'Cat B'
  elif a == b:
    return 'Mouse C'


print(catAndMouse(1, 3, 2))