class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_car(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_car = Car("BMW", "X5")
print(my_car.show_car())

my_Ecar = ElectricCar("BMW", "i7", "85kWh")
print(my_Ecar.show_car())