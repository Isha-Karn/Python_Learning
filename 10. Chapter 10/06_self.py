class Employee:
    company="Google"
    def getsalary(self):
        #print ("salary is 100k")
        print(f"salary for this employee working in {self.company} is {self.salary}")
isha= Employee()
isha.salary= 100000
isha.getsalary() # Employee.getsalary(isha) # we can write like this also