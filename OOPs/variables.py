

class Car:

    #class variable
    wheels = 4

    def __init__(self):
        #they're instance variables
        self.mil = 10
        self.comp = "BMW" 


c1 = Car()
c2 = Car()

c1.mil = 8

print(c1.comp, c1.wheels)
