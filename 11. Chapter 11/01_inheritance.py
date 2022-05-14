class Employee:         # base class or parent class
    company="Google"

    def showDetails(self):
        print("This is an employee")
 
class Programmer(Employee):     # derived class or child class
 language= "Python"

 def getLanguage(self):
     print(f"The language is {self.language}")

 def showDetails(self):
        print("This is a programmer")

e=Employee()
p=Programmer()
e.showDetails()
p.showDetails()
print(p.company)
