class Animals:
    def __init__(self):
        print("There are two types of animals\n(1)Wild animals\n(2)Domestic animals")
        
class Pets(Animals):
    
    def __init__(Self):
        super().__init__()
        print("Domestic animals are also called pets. Pets are very lovable")

class Dogs(Pets):
    
    def __init__(self):
        super().__init__()
        print("Dogs are the pets which bark.")

#a=Animals()
#p=Pets()
d=Dogs()

#Harry method
class Animal:
    animaltype="Mammal"

class Pets:
    colortype= "White"

class Dogs:
    @staticmethod
    def bark():
        print("Bow Bow!")

d= Dogs()
d.bark()


