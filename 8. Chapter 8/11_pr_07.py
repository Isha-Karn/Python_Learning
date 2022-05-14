def remove_and_split(string,word):
    newstr= string.replace(word, "")
    return newstr.strip()
this= "   Isha is a good girl  "  # strip means to remove blank spaces from the function.
n= remove_and_split(this, "Isha")
print(n)
    
