class Employee:
    company = "DELL"

    def __init__(self, salary, name, bond):
        self.salary = salary
        self.name = name 
        self.bond = bond

    def getSalary(self): # self is a way to reference the object of a class
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")
    
e1 = Employee(38000, "nooby", 4)
print(e1.get_info())
print(Employee.company) # always a class attribute printed
# object introspection
# print(dir(e1))

class Computer:

    def __init__(self, cpu, ram):
        # print("init")
        self.cpu = cpu
        self.ram = ram


    def config(self):
        print("config is: ", self.cpu, self.ram, "gb ram")

comp1 = Computer()
print(type(comp1))
# Computer.config(comp1)
comp1.config()

