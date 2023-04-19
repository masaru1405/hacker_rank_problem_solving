'''
Exemplo:
a = [2, 4]
b = [16, 32, 96]
-Seja x o valor que respeita as duas condições dadas no problema. O valor de x será o divisor para o valores do array 'b' e será o dividendo para os valores do array 'a'.
-Logo, x não poderá ser maior que o último elemento de 'a' e não poderá ser maior que o primeiro elemento de 'b'.
'''

def getTotalX(a, b):
  a.sort()
  b.sort()
  min_ = a[-1]
  max_ = b[0]
  resp = []
  value = min_

  while value <= max_:
    eh_divisor = True
    eh_dividendo = True
    for i in b:
      if i % value != 0:
        eh_divisor = False
        break
    if eh_divisor:
      for j in a:
        if value % j != 0:
          eh_dividendo = False
          break
    if eh_dividendo and eh_divisor:
      resp.append(value)
    value += 1
  
  print(resp)
  return len(resp)


a = [2, 4]
b = [16, 32, 96]

c = [3, 9, 6]
d = [36, 72]
print(getTotalX(c, d))