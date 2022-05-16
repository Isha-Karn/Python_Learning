list= []
while(True):
    item= input("Enter what items did you buy?")
    quan= (input("Enter the amount of the item: "))
    cost= int(input("Enter the cost of the item: "))
    choice  =   input("Do you want to add more items? ")
    list.append([item, quan, cost])
    if choice== "n":
        with open("expenses.txt","a")as f:
            for i in list:
                f.write(f" bought {i[0]} {i[1]} at Rs{i[2]}\n ")
                print(f" bought {i[0]} {i[1]} at Rs{i[2]}\n ")
                # [f.write(f" bought {i[0]} {i[1]} at Rs{i[2]}\n ") for i in list]--> list comprehension
        
        break