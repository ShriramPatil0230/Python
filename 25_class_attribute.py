class Employee:
    company = "Google"

sr = Employee()    
sr.company
sr.salary = 40000   #Adding instance Attribute
Employee.company = "YouTube" #Class Changing Attribute
print(sr.salary)
print(sr.company)