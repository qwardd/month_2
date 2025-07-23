# родительский, суперкласс
class Car:
    # инициализатор
    def __init__(self, model, year):
        # свойства, атрибуты, поля
        print("Вызов init в классе Car")
        self.model = model
        self.year = year
        self.fined = False

    def drive_to_location(self, location):
        print(f"Driving Car {self.model} to {location}")

# дочерний, наследник, подкласс, subclass
class Truck(Car):
    def __init__(self, model, year, max_weight):
        super().__init__(model, year)
        self.max_weight = max_weight

    def drive_to_location(self, location):
        print(f"Driving Truck {self.model} to {location}")

class Bus(Car):
    def drive_to_location(self, location):
        print(f"Bus {self.model} is driving to {location}")

truck_man = Truck("MAN", 2019, 3000)
print("Model", truck_man.model, "Year", truck_man.year, "fined", truck_man.fined)
truck_man.drive_to_location("Кант")
bus = Bus("Mercedes", 2024)

for car in (truck_man, bus):
    car.drive_to_location("Каракол")

# print(type(truck_man) == Car) # False
# print(isinstance(truck_man, Truck))
# print(isinstance(truck_man, Car))
# print(issubclass(Truck, Car))



class Furniture:
    pass

class Table(Furniture):
    pass

class Chair(Furniture):
    pass