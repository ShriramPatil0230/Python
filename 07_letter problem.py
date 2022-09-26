letter = '''Dear <|Name|>,
Your selected for this job ,
this is your joinig letter.
Date: <|DATE|>'''

name = input("Enter your name:\n ")
date = input("Enter your date:\n ")

letter = letter.replace("<|Name|>" , name)
letter = letter.replace("<|DATE|>" , date)
print(letter)


    
