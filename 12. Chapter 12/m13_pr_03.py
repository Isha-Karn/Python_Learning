from pip import main


a= int(input("Enter any number:"))
b=[a*i for i in range(1,11) ]
print(b)

with open("table.txt", "a") as f:
    f.write(str(b))
    f.write ("\n")

