def migratoryBirds(arr):
  lista_frequencia = [0, 0, 0, 0, 0]
  for i in range(len(arr)):
    if(arr[i] == 1):
      lista_frequencia[0] += 1
    elif(arr[i] == 2):
      lista_frequencia[1] += 1
    elif(arr[i] == 3):
      lista_frequencia[2] += 1
    elif(arr[i] == 4):
      lista_frequencia[3] += 1
    elif(arr[i] == 5):
      lista_frequencia[4] += 1
  
  max_freq = 0
  index = 0
  for j in range(len(lista_frequencia)):
    if(lista_frequencia[j] > max_freq):
      max_freq = lista_frequencia[j]
      index = j
  
  return index+1 #pq lista comeca do index 0, mas o id dos passaros comeca do 1

teste = [1,4,4,4,5,3]
teste2 = [1,1,2,2,3]
teste3 = [1,2,3,4,5,4,3,2,1,3,4]
resp = migratoryBirds(teste3)
print(resp)