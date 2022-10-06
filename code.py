x=input()
y=int(input(""))
c=""
for i in x:
    for j in range (y):
        c=c+i
    if c in x:
        x=x.replace(c,"")
    c=""
print(x)            