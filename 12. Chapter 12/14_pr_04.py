try:
    a= int(input("Enter any number: "))
    b= int(input("Enter any number: "))
    c=a/b
    print (c)
except ZeroDivisionError as e:
    print ("The value is infinite.")

#my method:
a= int(input("Enter any number: "))
b= int(input("Enter any number: "))
try:
        print(a/b)
except:
    print ("Infinite")

