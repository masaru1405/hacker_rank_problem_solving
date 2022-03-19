def timeConversion(s):
  #07:05:45PM
  time = s[0:-2].split(':') # do início até o penúltimo, tira AM/PM e depois tira o ':'
  am_pm = s[-2:] # guarda AM/PM
  temp = time[1] + ":" + time[2]

  if am_pm == "AM":
    if time[0] == "12":
      resp = "00:" + temp
    else:
      resp = time[0] + ":" + temp
  else:
    if time[0] == "12":
      resp = "12:" + temp
    elif time[0] == "01":
      resp = "13:" + temp
    elif time[0] == "02":
      resp = "14:" + temp
    elif time[0] == "03":
      resp = "15:" + temp
    elif time[0] == "04":
      resp = "16:" + temp
    elif time[0] == "05":
      resp = "17:" + temp
    elif time[0] == "06":
      resp = "18:" + temp
    elif time[0] == "07":
      resp = "19:" + temp
    elif time[0] == "08":
      resp = "20:" + temp
    elif time[0] == "09":
      resp = "21:" + temp
    elif time[0] == "10":
      resp = "22:" + temp
    elif time[0] == "11":
      resp = "23:" + temp
  return resp

s = "07:05:45PM"
resp = timeConversion(s)
print(resp)