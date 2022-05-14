def fact(num):
    f=1
    for i in range(1, num+1):
        f=f*i
    return(f)

def factTrailingZero(num):
    c=0
    while(num%10==0):
        c=c+1
        num=num/10
    return (c)

print(fact(20))
print (factTrailingZero(fact(20)))