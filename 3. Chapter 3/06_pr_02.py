letter= '''Dear <|Name|>,
You are selected!
Date:<|Date|> '''
name= input("Enter your name\n")
Date= input("Enter date\n")
letter= letter.replace("<|Name|>", name)
letter= letter.replace("<|Date|>", Date)
print(letter)