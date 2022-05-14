class Calculator:
    def __init__(self, num):
        self.num= num
    
    def square(self):
        print(f"The square of the {self.num} is {self.num ** 2}") # here ** represents ^2

    def squareRoot(self):
        print (f"The squareroot of {self.num} is {self.num ** 0.5}")

    def cube(self):
        print(f"The cune of the {self.num} is {self.num **3}")

    @staticmethod 
    def greet():
      print("****Hello to the world of calculator****")

a= Calculator(36)
a.greet()
a.square()
a.squareRoot()
a.cube()
