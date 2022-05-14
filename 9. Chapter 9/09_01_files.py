# Use open fuction to read the content of file!
# f= open('sample.txt', 'r')
f= open('sample.txt') # by default the mode is r
# data= f.read()
data= f.read(8) # reads only 8 characters.
print(data)
f.close()