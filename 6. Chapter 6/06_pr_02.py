from ast import Or


a= int(input("Enter the marks of 1st subject: "))
b= int(input("Enter the marks of 2nd subject: "))
c= int(input("Enter the marks of 3rd subject: "))
if (a<33 or b<33 or c<33):
    print("You are fail because you have less than 33% in one of the subject")
if (a+b+c)/3 <40:
    print("You are fail due to the percentage less than 40")
else:
    print("You are pass")

    


