def birthday(s, d, m):
  resp = 0
  if(len(s) <= m):
    for i in range(len(s)): #itera sobre toda a lista
      j = i
      k = 0 
      temp_sum = 0
      while(k < m): #itera sobre a lista, andando de m em m
        temp_sum += s[j]
        j += 1
        k += 1
      if(temp_sum == d):
        resp += 1

    return resp

  else:
    #ver obs
    for i in range((len(s)+1) - m): #itera sobre toda a lista
      j = i
      k = 0 
      temp_sum = 0
      while(k < m): #itera sobre a lista, andando de m em m
        temp_sum += s[j]
        j += 1
        k += 1
      if(temp_sum == d):
        resp += 1

    return resp

#OBS:
'''
Pegando como exemplo o TESTE 1: 
range(len(s) - m) ==> range(5 - 2) = range(3) = (0,3) ==>[0,1,2], não vai até o index 3, por isso somamos +1 
'''
#TESTE 1
lista1 = [1, 2, 1, 3, 2]
#dia = 3
#mes = 2

#TESTE 2
lista2 = [4]
#dia = 4
#mes = 1

#TESTE 3
lista3 = [2,5,1,3,4,4,3,5,1,1,2,1,4,1,3,3,4,2,1]
dia = 18
mes = 7
output = 3

r = birthday(lista3, 18, 7)
print(r)
print(len(lista3))