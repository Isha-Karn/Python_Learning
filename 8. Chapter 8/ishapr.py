#n=3
#for i in range(3):
#    if i!=0 and i!=n-1:
#        print("*" + " " * (n-2)+ "*")
#    else:
#        print("*" * n)

n=3
for i in reversed(range(3)):
    print(" " *  (n-i-1), end= " ")
    print("*" * (2*i+1), end= " ")
    print(" " * (n-i-1))

