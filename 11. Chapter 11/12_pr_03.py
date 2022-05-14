class Employee:             # totalsalary= salary * increment
    salary= 1000
    increment= 1.5

    @property
    def totalSalaryAfterIncrement(self):
        return self.salary*self.increment

    @totalSalaryAfterIncrement.setter
    def totalSalary(self,val):
        self.increment= val/self.salary
    
e=Employee()
print (e.totalSalaryAfterIncrement)
e.totalSalary= 2000
print(e.increment)
     
