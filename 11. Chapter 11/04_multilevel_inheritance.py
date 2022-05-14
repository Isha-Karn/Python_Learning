class Person:
    country= "Nepal"

    def getBreath(self):
        print("I am breathing.")

class Employee(Person):
    company="Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def getBreath(self):
        print("I am an employee so I am luckily breathing.")

class Programmer(Employee):
    company= "Fiverr"

    def getSalary(self):
        print("No salary to programmers")

p= Person()
p.getBreath()
# print(p.comapny) #throws an error

e= Employee()
e.getBreath()
print(e.company)
print (p.country)

pr= Programmer()
pr.getBreath()  # This will print the latest one
print(pr.company)
print(pr.country)