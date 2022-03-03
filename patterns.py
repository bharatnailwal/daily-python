#Approch
# 1 > run the outer for loop [rows]
# 2 > Identofy, every row numbers, how many colums are there
# 3 > types of elements in the colums, wghat do you need to print

# x x x x x x x x x x 
# x x x x x x x x x x 
# x x x x x x x x x x 
# x x x x x x x x x x 
# x x x x x x x x x x 
# x x x x x x x x x x 
# x x x x x x x x x x 
# x x x x x x x x x x 
# x x x x x x x x x x 
# x x x x x x x x x x 


def patterns(num):
    for i in range(num):
        for j in range(num):
            print ("x",end=' ')
        print()


print(patterns(10))


# x 
# x x 
# x x x 
# x x x x 
# x x x x x 
# x x x x x x 
# x x x x x x x 
# x x x x x x x x 
# x x x x x x x x x 
# x x x x x x x x x x 

def patterns(num):
    for i in range(num):
        for j in range(i+1):
            print ("x",end=' ')
        print()

print(patterns(10))




# x x x x x x x x x x 
# x x x x x x x x x 
# x x x x x x x x 
# x x x x x x x 
# x x x x x x 
# x x x x x 
# x x x x 
# x x x 
# x x 
# x 


def patterns(num):
    for i in range(num):
        for j in range(i,num):
            print ("x",end=' ')
        print()
        
print(patterns(10))




# x                     
# x x                   
# x x x                 
# x x x x               
# x x x x x             
# x x x x x x           
# x x x x x x x         
# x x x x x x x x       
# x x x x x x x x x     
# x x x x x x x x x x  


def patterns(num):
    for i in range(num):
        # for j in range(i,num):
        #      print (" ",end=' ')
        for j in range(i+1):
            print ("x",end=' ')
        for j in range(i,num):
            print (" ",end=' ')
        print()
        
print(patterns(10))



#                     x 
#                   x x 
#                 x x x 
#               x x x x 
#             x x x x x 
#           x x x x x x 
#         x x x x x x x 
#       x x x x x x x x 
#     x x x x x x x x x 
#   x x x x x x x x x x 

def patterns(num):
    for i in range(num):
        for j in range(i,num):
            print (" ",end=' ')
        for j in range(i+1):
            print ("x",end=' ')
        print()
        
print(patterns(10))
