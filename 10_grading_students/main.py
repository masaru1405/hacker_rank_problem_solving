def gradingStudents(grades):
  resp = []
  for i in grades:
    if i < 38:
      resp.append(i)
    else:
      temp = i % 5
      if temp != 0:
        diff = 5 - temp
        if diff < 3:
          resp.append(i + diff)
        else:
          resp.append(i)
      else:
        resp.append(i)
  return resp

notas = [73, 67, 38, 33]
resp = gradingStudents(notas)
print(resp)