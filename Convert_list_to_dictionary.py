def Convert(lst):
  dt = {}
  for i in lst:
    if i in dt:
      dt[i]+=1
    else:
      dt[i]=1
  return dt       
# Driver code
lst = ['a', 'a', 'b', 'f', 'c', 'l']
print(Convert(lst))
