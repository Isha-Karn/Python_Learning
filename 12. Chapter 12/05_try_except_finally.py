try:
    a=int(input("Enter any number: "))
    c=1/a
except Exception as e:
    print(e)
    exit()
finally:
    print("We are done.") # keeps on appearing even if the program throws an error and even 
  #if u exit the program.
print("Thanks for using the program.")