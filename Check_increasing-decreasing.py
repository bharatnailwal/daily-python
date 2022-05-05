# to heck if the numbers in the array are increaing order or decreasing
array=[1,1,2,3,4,4,5,5,3333,3] 
temparray=sorted(array) 
if(temparray==array): 
    print("The array is Increasing") 
else: 
    temparray=sorted(array) 
    temparray.sort(reverse=1) 
    if(temparray==array): 
        print("The array is Increasing") 
    else: 
        print("The array is Decreasing") 
