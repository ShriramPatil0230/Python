from tokenize import Number

while(True):
        print("Enter q for Quit")
        a =input("Enter your Number: ")
        if a == 'q':
            break 
        try:   
            print("Trying.....")
            a = int(a)
            if (a>6):
                print("Number Is greater then 6")
            else:
                print("Number is Smaller then 6")
        except Exception as e:
            print(f"Please Enter Right Input(integer){e}")    

print("Thank you for Playing")