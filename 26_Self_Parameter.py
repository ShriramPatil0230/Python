class Employee:
    company = "Google"

    @staticmethod
    def greet():
        print("Hello SR")
    def getSalary(self):
        print(f"Salary for this Employee working in {self.company}:{self.salary}")
    
sr = Employee()
sr.salary = 40000   
sr.greet()
sr.getSalary()