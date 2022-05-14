a=[3,5,8,6,88,54,89]
#b=[]
#for i in a:
 #if i%2==0:
  #  b.append(i)
#print (b)
 
b=[i for i in a if i%2==0]
print(b)