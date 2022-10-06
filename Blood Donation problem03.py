# Blood Donation program by using nested if statment
print("***********WELL COME TO BLOOD DONATION CAMP***********")
Age=int(input("Enter Your Age:"))
bloodgroup=("A,A-,B,B-,AB,AB-,O,O-") #select blood group
if Age>18:
    Bloodgroup=input("Enter Your Blood Group:")
    if Bloodgroup in bloodgroup:
        print("Your Eligible to Donate Blood")
        print("Now You Can Donate Your Blood")
        print("Thank You For Donating Blood ")
    else:
        print("Blood group not match")    
else:
   print("Your Not Eligible")    
