from fileinput import lineno


with open("logfile.txt") as f:
    content= f.read()
if 'python' in content:
    print("Yes, python is present")
else:
    print("Python is not present")