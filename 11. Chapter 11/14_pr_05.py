class Vector:
    def __init__(self, vec):
        self.vec=vec
    
    def __str__(self):
        str1= ""
        index =0
        for i in self.vec:
            str1 += f"{i}a{index} +"
            index +=1
        return str1[:-1]

    def __add__(self,vec2):
        if len(self.vec)== len(vec2.vec):
            newlist=[]
            for i in range(len(self.vec)):
                newlist.append(self.vec[i]+vec2.vec[i])
            return Vector(newlist)
        else:
            return ("addition failed as the two vector length mismatch")


    def __mul__(self,vec2):
        if len(self.vec)== len(vec2.vec):
            sum=0
            for i in range(len(self.vec)):
                sum += self.vec[i]*vec2.vec[i]
            return sum
        else:
            return ("The dimension of two vectors are not equal")
            
v1= Vector([1,2,3])
v2= Vector([1,5,6,9])
print(v1)
print(v1+v2)
print(v1*v2)
