import csv

name=input("Enter your name:")
p =int(input("Enter your percentage:"))

if p>=70 and p<=100:
    print("distinction")

elif p>=65 and p<70:
    print("1st class")
elif p>=50 and p<65:
    print("2nd class")
elif p>=35 and p<50:
    print("Pass")
elif p>100:
    print("Please Enter Correct Percentage")    
else:
    print("fail")

with open("students records.csv","r") as f:
    studentRecords= f.read()
with open("students records.csv","a") as f:
    f.write(str("\n" +name +":"))
    f.write(str(str(p)))