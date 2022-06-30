

def fitness():
    w= float(input("Enter your weight in kg: "))
    h= float(input("Enter your height in meter: "))
    BMI= (w/h**2)
    print (BMI)
    if BMI<18.5:
        print("**You are underweight**")
    if BMI>18.5 and BMI<24.9:
        print("**Your BMI is normal**")
    if BMI>25 and BMI<29.9:
        print("**You are overweight**")
    if BMI>30:
        print("**You have obesity. Please loose your weight and do exercise**")
    
fitness()

