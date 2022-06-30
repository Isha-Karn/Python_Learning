with open("currencyData.txt") as f:
	lines= f.readlines()

currencyDict={}
for line in lines:
	parsed= line.split("\t")
	currencyDict[parsed[0]]= parsed[1]

amount= int(input("Enter the amount: "))
print("Choose the currency you want to convert. The available options are:")
[print(item) for item in currencyDict.keys()]
currency= input("choose one of these: ")
print(f"{amount} NPR is equal to {amount*float(currencyDict[currency])} {currency}")
