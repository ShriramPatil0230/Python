Number =6

for Number in range(1,Number+1):
    print("*"*Number)

Number =6
What = input("Enter what do you want to print:")

for Number in range(1,Number+1):
    print(What*Number)      

Number =6
What = input("Enter what do you want to print:")

for Number in range(Number,0,-1):
    print(What*Number)
    
    # lets join both program 

Number =6
ToPrint = "1"
for Number in range(1,Number+1):
    print(ToPrint*Number)      

for Number in range(Number -1,0,-1):
    print(ToPrint*Number)              