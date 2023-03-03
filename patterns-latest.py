count=int(10)
k=0
for i in range(1,count+1):
    for j in range(1,(count-i)+1):
        print(end= "  ") ## play with this line to move the pyramid
    while k!=(2*i-1):
        print("* ",end="")
        k+=1
    k=0
    print()
