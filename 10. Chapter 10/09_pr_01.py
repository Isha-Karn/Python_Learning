class Programmer:
    company= "Microsoft"

    def __init__(self, name, product):
         self.name= name
         self.product= product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the name of the product is {self.product}")

isha= Programmer("Isha", "Skype")
ishan= Programmer ("Ishan", "Github")
isha.getInfo()
ishan.getInfo() 