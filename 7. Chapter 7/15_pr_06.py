# n!= 1 * 2 * 3 * 4 * .... * n
num= int(input("Enter any number: "))
factorial= 1
for i in range(1, num+1):
    factorial= factorial * i
print ("The factorial of the given number is: ", factorial)

