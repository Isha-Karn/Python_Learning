num= int(input("Enter any number: "))
prime= False
for i in range(2, num): #prime number is a number whose factor is either 1 or that number only. 
                        # 5 ko factor 5 ani 1 matraho bt 4 ko factor 2 pni ho. 2*2=4 and 4*1=4
    if (num%i==0):
        prime= True
        break #nalagayeni hunxa
if prime:
    print("This is a prime number")
else:
    print("This is not a prime number")
        
    