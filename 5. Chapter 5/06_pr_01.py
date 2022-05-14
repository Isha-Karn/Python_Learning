mydict = {
    "khao" : "Eat",
    "suto" : "sleep",
    "khelo" : "play"
}
print("The options are", mydict.keys())
a= input ("Enter the Hindi word\n")
 # print("The meaning of your word is", mydict[a]) # Creates an error when key is not in the dictionary

 # Below line will not create an eror if the key is not in the dictionary
print("The meaning of your word is", mydict.get(a))
