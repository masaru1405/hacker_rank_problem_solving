def pageCount(n, p):
  lista = list(range(n)) #transforma numa lista de 0 até n-1
  lista.append(n) #add o ultimo elemento

  pages_from_start = 0
  pages_from_final = 0

  #start from page 1
  if p != 1: #não é a primeira página
    if p % 2 == 0: #página buscada é par
      i = 0
      while i < n:
        if lista[i] == p:
          break
        i += 2
        pages_from_start += 1
    else: #página buscada é ímpar
      i = 1
      while i < n:
        if lista[i] == p:
          break
        i += 2
        pages_from_start += 1
  else: #página buscada é a primeira página
    return pages_from_start

  #start from last page
  j = n
  if p == j: #a pagina buscada é a ultima
    return pages_from_final
  elif n % 2 == 0: #ultima pagina é par
    if p % 2 == 0: #pagina buscada é par 
      while j > 0: 
        j -= 2
        pages_from_final += 1
        if lista[j] == p:
          break    
    else: #pagina buscada é impar
      while j > 0: 
        j -= 2
        pages_from_final += 1
        if lista[j+1] == p:
          break
  else: #ultima pagina é impar
    if p % 2 == 0: #pagina buscada é par
      while j > 0: 
        if lista[j-1] == p: #vê a pagina vizinha sem virar a pagina
          break
        j -= 2 
        pages_from_final += 1 #agora virou a pagina
    else: #pagina buscada é impar
      while j > 0:
        j -= 2
        pages_from_final += 1
        if lista[j] == p:
          break    

  print(pages_from_start, " ", pages_from_final)
  return min(pages_from_start, pages_from_final)

#Testes:
#pageCount(7, 4) ==> resp: 
#pageCount(70809, 46090) ==> resp: 12359
#pageCount(96993, 70030)  ==> resp: 13481
#pageCount(18183, 18042) ==> resp: 70

resp = pageCount(18183, 18042)
print(resp)

#[0,1,2,3,4,5,6]