'''
PascalCase:   #P and C is capital
EmployeeName --> PascalCase

camelcase:
isnumeric, isfloatOrInt --> camelCase  #only first word is small 

''' 

#a= 12
##b=34
#print ("The sum of num is:", a+b)

# Using oop
class Number:
    def sum(self):
        return self.a+ self.b
num = Number()    # object initiation
num.a= 12
num.b= 34
s= num.sum()
print(s)


