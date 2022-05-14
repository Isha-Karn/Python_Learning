class Number:
    def __init__(self,num):
        self.num=num

    def __add__(self, num2):
        print("Let's add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Let's multiply")
        return self.num* num2.num 

    def __truediv__(self, num2):
        print("Let's divide")
        return self.num / num2.num

    def __str__(self):
      return f"Decimal number: {self.num}"

    def __len__(self):
        return 1

n= Number(8)
print(n)
print(len(n))


