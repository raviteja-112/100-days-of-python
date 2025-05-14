text = input("Enter the comment:")
if('make a lot of money'or'buy now'or'subscribe this'or 'click this' in text):
    spam = True
if (spam == True):
    print('your text has spam content')
else:
    print('your text doesnt has spam content')
