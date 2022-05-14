while (True):
    print("q to exit the game.")
    a= input("Enter any number:")
    
    if a== 'q':
        break

    try:
        a= int(a)
        if a>6:
            print("You have entered the greater number.")
    except Exception as e:
        print (f"Your input resulted as an error: {e}")

print ("Thanks for playing the game.")