def dayOfProgrammer(year):
  if year <= 1917:
    if year % 4 == 0:
      return "12.09.{}".format(year)
    else:
      return "13.09.{}".format(year) #ano não bissexto
  elif year == 1918:
    return "26.09.{}".format(year) #"14 dias a mais"
  else:
    if(year % 400 == 0):
      return "12.09.{}".format(year)
    elif((year % 4 == 0) and (year % 100 != 0)):
      return "12.09.{}".format(year)
    return "13.09.{}".format(year) #ano não bissexto



#testes
resp = dayOfProgrammer(1700)
print(resp)