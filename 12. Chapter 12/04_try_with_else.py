try:
    a=int(input("Enter any number: "))
    c=1/a
except Exception as e:
    print(e)
else:
    print(c)
    print("We were successful.")