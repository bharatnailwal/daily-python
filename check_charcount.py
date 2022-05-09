def charcount(name):
    dct = {}
    for i in name:
        if i in dct:
            dct[i] +=1
        else:
            dct[i] = 1
    return dct

name = "hellow"  
dct = charcount(name)
print(dct)
