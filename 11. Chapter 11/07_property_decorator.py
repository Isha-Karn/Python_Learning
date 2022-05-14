class Employee():
    company="Google"
    salary= 5600
    bonus=500
    #totalsalary=6100

    @property
    def totalSalary(self):
        return self.salary+self.bonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.bonus= val-self.salary

e= Employee()
print(e.totalSalary) 
e.totalSalary=5800
print(e.salary)
print(e.bonus)