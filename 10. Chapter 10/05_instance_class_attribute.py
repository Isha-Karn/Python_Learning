class Employee:
    company= "Google" #yo class ko attribute ho
    salary=100

isha= Employee()
ishan= Employee()
#creating instance attribute salary for both the objects
#isha.salary= 16  #print will first look through the instance attribute of the object and the
                    #   it will print this line
#ishan.salary=35
isha.salary=16
print(isha.salary)
print(ishan.salary)

#throws an error as address is not present in the present class
 # print(ishan.address)