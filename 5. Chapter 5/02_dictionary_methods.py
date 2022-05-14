myDict = {
"fast" : "In a quick manner",
"isha" : "A good girl",
"marks" : [1,2,9],
"anotherdict" : {'Isha' :'Kind girl'},
 1 : 2
}
# Dictionary methods
print(list(myDict.keys())) # prints the keys of the dictionary
print(myDict.values()) # prints the values of the dictionary
print(myDict.items()) # prints (key, value) for all the items of the dictionary
print(myDict)
updateDict = {
    "Lovish" : "Parents",
    "ram" : "shyam",
    "sita" : "gita",
    "isha" : "a singer"
}
myDict.update(updateDict)  # Updates the dictionary by adding key-value pairs from the updateDict.
print(myDict)

print(myDict.get("isha")) # Prints value associated with the key isha
print(myDict["isha"]) # Prints value associated with the key isha

# The difference between .get and [] syntax in dictionaries?
print(myDict.get("isha2")) # Returns none as isha2 is not present in the dictionary
print(myDict["isha2"]) # throws error as isha2 is not present in the dictionary