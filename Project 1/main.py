import random
# snake, water or gun 
def gamewin(comp,you):
    if comp==you:
        return None
    if comp== 's':
         if you== 'g':
             return True
         elif you=='w':
           return False
    if comp=='g':
        if you== 's':
            return False
        elif you== 'w':
            return True
    if comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
print("Computer's turn: snake(s) water(w) or gun(g)?")
randomno= random.randint(1,3)  #1 dekhi 3 samma linxa..means 1,2,3
if randomno==1:
    comp= 's'
elif randomno==2:
    comp= 'w'
elif randomno==3:
    comp= 'g'
you= input("Your's turn:snake(s) water(w) gun(g)?")
print(f"Computer chose {comp}")
print (f"You chose {you}")
a= gamewin(comp,you)
if a== None:
    print("The game is tie")
if a== True:
    print("You win the game")
if a== False:
    print("You lose the game")






