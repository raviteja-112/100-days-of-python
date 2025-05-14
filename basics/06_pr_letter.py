letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|> '''
name = input("Enter you name :")
date = input("Enter date :")
letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)
print(letter)
