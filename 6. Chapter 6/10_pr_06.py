a= int(input("Enter your percentage:"))
if (a>=80 and a<90):
    print("A")
elif (a>=90 and a<100):
    print("Ex")
elif (a>=70 and a<80):
    print("B")
elif (a>=60 and a<70):
    print("C")
elif (a>=50 and a<60):
    print("D")
else:
    print("F")

# It is important to note that while use elif if their is multiple conditions then we must use and. example, 
# if we enter the number 95 then the program will check the first condition which shows 95 is greater than
# 80 and it will print grade A instead of EX

#a= int(input("Enter your percentage:"))
#if (a>=80 ):
#    print("A")
#elif (a>=90 ):
#    print("Ex")
#elif (a>=70 ):
#    print("B")
#elif (a>=60 ):
#    print("C")
#elif (a>=50 ):
#    print("D")
#else:
#    print("F")