class Student:

    def __init__(self, name, rollNo):
        self.name = name 
        self.rollNo = rollNo
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollNo)
        self.lap.show()
    class Laptop:

        def __init__(self):
            self.brand = 'Motorola'
            self.cpu = 'intel core 5'
            self.ram = 16

        def show(self):
            print(self.brand, self.cpu, self.ram)



s1 = Student("inte", 39)
s1.show()