from fileinput import lineno


content= True
i=1
with open("logfile.txt")as f:
    while content:
     content= f.readline()
     if 'python' in content:
         print(content)
         print (f"python is present in line number: {i}")

     i+=1