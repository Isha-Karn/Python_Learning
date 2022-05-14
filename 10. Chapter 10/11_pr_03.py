class sample:
    a= "Google" # This is class attribute

object= sample()
object.a= "Youtube" # This is instance attribute
#sample.a= "Youtube" # This will change the class attribute
#print(sample.a)
print(object.a)