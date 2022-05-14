class Employee:
    company= "Google" #yo class ko attribute ho

isha= Employee()
ishan= Employee()
isha.salary= 16
ishan.salary=35
print(isha.company)
print(ishan.company)

Employee.company= "Youtube" #class ko company change gareko
print(isha.company)
print(ishan.company)
print(isha.salary)
print(ishan.salary)