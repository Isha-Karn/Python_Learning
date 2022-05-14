class Employee:
    company="Google"

    def getsalary(self, signature):
        #print ("salary is 100k")
        print(f"salary for this employee working in {self.company} is {self.salary}\n {signature}")

    @staticmethod
    def greet(): # if u put self here then the fuction does not work
            print("Good Morning, Sir")

isha= Employee()
isha.salary= 100000
isha.getsalary("Thanks!")
isha.greet() #Employee.greet()