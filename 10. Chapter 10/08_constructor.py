class Employee:
    company="Google"

    def __init__(self, name, salary, subunit):
        self.name= name
        self.salary= salary
        self.subunit= subunit
        print("Employee is created")

    def getDetails(self):
            print (f"The name of the employee {self.name}")
            print (f"The salary of the employee {self.salary}")
            print (f"The subunit of the employee {self.subunit}")

    def getsalary(self, signature):
        #print ("salary is 100k")
        print(f"salary for this employee working in {self.company} is {self.salary}\n {signature}")

    @staticmethod
    def greet(): # if u put self here then the fuction does not work
            print("Good Morning, Sir")

isha= Employee("Isha", 100, "Printers")
isha.getDetails()
