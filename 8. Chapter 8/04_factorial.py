# n!= 1*2*3*4*....n
# n!= n*(n-1)!  # means if the number is 4 it becomes 4*(4-1)*.....
# n=5
# product= 1
# for i in range (1, n+1)
# product= product * i
# print (product)

# using function
def factorial_iter(n):
    product=1
    for i in range(1,n+1):
        product=product*i
    return product     # here return ended the execution of the function.
print(factorial_iter(5))

# using recursion
def factorial_recursion(n):
    if n==1 or n==0:
        return 1   # return 1 vaneko jaba n= 0 or 1 vayo vane 1 output dine ho because 1 ani 0 ko fact 1 ho
    return n* factorial_recursion(n-1)
print(factorial_recursion(6))

# sum of natural number using function
def sum(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    return s
print(sum(5))
