from pip import main


def greet(name):
    print(f"Good Morning, {name}")

#print(__name__)
if __name__== "__main__":

    a= input("Enter any name: ")
    greet(a)