#files In Python
f = open('s.txt', 'r')
data = f.read()
if 'Shriram' in data:
    print(data)
else:
    print("absent")    
f.close()



