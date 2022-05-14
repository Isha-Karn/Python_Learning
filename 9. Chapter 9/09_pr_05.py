words= ["isha","mote","rita"]

with open("donkey.txt","r")as f:
    a=f.read()

for word in words:
    a= a.replace(word, "######")
with open("donkey.txt", "w")as f:
      a= f.write(a)