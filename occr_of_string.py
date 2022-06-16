word = "i ,love india love"
dt = {}
wrd = word.split()
#print(wrd)


for i in wrd:
  sd = ""
  for j in i:
    if j == ",":
      continue
    else:
      sd += j
  if sd in dt:
    dt[sd] +=1
  else:
    dt[sd] = 1
print(dt)
