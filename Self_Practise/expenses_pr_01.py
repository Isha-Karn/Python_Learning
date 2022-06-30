def add():
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
                    f.write(f" bought {i[0]} {i[1]} at Rs{i[2]}\n")
                    print(f" bought {i[0]} {i[1]} at Rs{i[2]}")
                    # [f.write(f" bought {i[0]} {i[1]} at Rs{i[2]}\n ") for i in list]--> list comprehension
            
            break

def view():
    with open ("expenses.txt")as f:
        a= f.readlines()
        [print (i) for i in a]

def main():
    print("Press 1 to add data or press 2 view data")
    a= int(input("Enter your choice: "))
    if a== 1:
        add()
    else:
        view()

        
main()

