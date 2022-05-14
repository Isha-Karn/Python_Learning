class Person:
    country= "Nepal"

    def __init__(self):
        print("Initializing person..\n")

    def getBreath(self):
        print("I am breathing.")

class Employee(Person):
     company="Honda"

     def __init__(self):
         super().__init__()
         print("Initializing employee..\n")

     def getSalary(self):
        print(f"Salary is {self.salary}")
    
     def getBreath(self):
        super().getBreath()
        print("I am an employee so I am luckily breathing.")

class Programmer(Employee):
    company= "Fiverr"

    def __init__(self):
         super().__init__()
         print("Initializing programmer..\n")


    def getSalary(self):
        print("No salary to programmers")
    
    def getBreath(self):
        super().getBreath()
        print("I am a programmer so i am breathing++")

#p= Person()
#p.getBreath()

#e= Employee()
#e.getBreath()

pr= Programmer()
#pr.getBreath()  # This will print the latest one
