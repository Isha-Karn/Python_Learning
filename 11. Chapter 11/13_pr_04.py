# (a+bi) (c+di)= (ac-bd)+(ad+bc)i
class Complex:
    def __init__(self,r,i):
        self.real= r
        self.imaginery= i

    def __add__(self,c):
        addReal= self.real+c.real
        addImg= self.imaginery+c.imaginery
        return Complex(addReal,addImg)

    def __mul__(self,c):
        mulReal= self.real*c.real- self.imaginery*c.imaginery
        mulImg= self.real*c.imaginery+ self.imaginery*c.real
        return Complex(mulReal,mulImg)

    def __str__(self):
        if self.imaginery<0:
            return f"{self.real}-{-self.imaginery}i"
        else:
            return f"{self.real}+{self.imaginery}i"

C1= Complex(3,2)
C2= Complex (1,7)  # (3x1-2x7)= -11
print (C1+C2)       # (3x7+2x1)= 23
print(C1*C2)
