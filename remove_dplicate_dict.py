eg_dic={1:1,2:2,3:2,4:3}
res = {}
print("The original dictionary is:",eg_dic)
for key,val in eg_dic.items():  
  if val not in res.values():
    res[key]=val
print("The dictionary after removing the duplicates is:",res)
