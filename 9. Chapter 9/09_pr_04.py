with open("donkey.txt","r")as f:
    a=f.read()

    a= a.replace("donkey", "######")
with open("donkey.txt", "w")as f:
    a= f.write(a)