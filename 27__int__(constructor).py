class Employee:
     def __init__(self,name):
         self.name = name

     def getSalary(self):
         print(f"Salary is {self.salary}")

sr = Employee("sr")
sr.salary=40000
sr.getSalary()             
        