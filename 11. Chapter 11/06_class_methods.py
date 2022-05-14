class Employee:
    company= "Camel"
    salary= 100
    location= "Biratnagar"

    #def changeSalary(self,sal):
    #    self.__class.__.salary= sal

    @classmethod
    def changeSalary(cls,sal):
        cls.salary= sal

e= Employee()
print(e.salary)
e.changeSalary(4555)
print(e.salary)
print(Employee.salary) 