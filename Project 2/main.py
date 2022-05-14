import random
randomno=random.randint(1,100)
userguess=None
guess=0

while userguess !=randomno:
    userguess= int(input("Enter the number between 1 to 100: "))
    
    if userguess==randomno:
        print("your guess is right.")
    else:
        if userguess<randomno:
         print("Your guess is wrong, enter higher number")
        else:
            print("Your guess is wrong,enter lower number")
    guess +=1
print(f"you have guessed {guess} times")

with open("highscore.txt", "r") as f:
    highscore= int(f.read())

if highscore>guess:
    print("You have just broken the high score")
    with open("highscore.txt","w") as f:
     f.write(str(guess))



