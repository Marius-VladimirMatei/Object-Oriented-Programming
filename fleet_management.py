

from abc import ABC, abstractmethod


# Base Class for all Motorized and NonMotorized
class Vehicle(ABC):
    totalVehicles = 0 # Class attribute that tracks the total number of vehicles

    # def __init__ constructor to initialize the attributes
    def __init__(self, id, license_plate, brand, model):
        self.id = id
        self.license_plate = license_plate
        self.brand = brand
        self.model = model

        Vehicle.totalVehicles +=1 # Increment total vehicles when a new vehicle is created

    @abstractmethod # Abstract method to enforce implementation in subclasses.
    def drive(self):
        pass

    @abstractmethod # Abstract method to enforce implementation in subclasses.
    def maintain(self):
        pass

    @staticmethod # utility function decorator: the function does not require access to instance or self. parameter
    def show_totalVehicles():
        return f"There are {Vehicle.totalVehicles} vehicles."

    @staticmethod
    def general_usage():
        return "Vehicles are used to transport people or goods."



# Inherits from Vehicle. Is the Parent Class for Car, CargoTruck and Motorcycle
class Motorized(Vehicle):
    def __init__(self, id, license_plate, brand, model, fuel_type):
        # super().__init__ initializes the attributes form the Parent Class
        super().__init__(id, license_plate, brand, model)
        self.fuel_type = fuel_type

    def drive(self):
        return f"{self.brand} {self.model} is driving with a motor."

    def refuel(self):
        return f"{self.brand} {self.model} is being refueled."

    def maintain(self):
        return f"{self.brand} {self.model} undergoing regular maintenance. "


# Inherits from Vehicle. Is the Parent Class for Bicycle
class NonMotorized(Vehicle):
    def __init__(self, id, license_plate, brand, model, type):
        super().__init__(id, license_plate, brand, model)
        self.type = type # "manual" or "electric"

    def drive(self):
        return f"{self.brand} {self.model} {self.type} is powered by human effort."

    def maintain(self):
        return f"{self.brand} {self.model} {self.type} is being checked for wear and tear."


class Car(Motorized):
    def __init__(self, id, license_plate, brand, model, fuel_type, number_of_doors, air_conditioning):
        super().__init__(id, license_plate, brand, model, fuel_type)
        self.number_of_doors = number_of_doors
        self.air_conditioning = air_conditioning

class CargoTruck(Motorized):
    def __init__(self, id, license_plate, brand, model, fuel_type, load_capacity):
        super().__init__(id, license_plate, brand, model, fuel_type)
        self.load_capacity = load_capacity
        self.current_load = 0


class Motorcycle(Motorized):
    def __init__(self, id, license_plate, brand, model, fuel_type, engine_capacity):
        super().__init__(id, license_plate, brand, model, fuel_type)
        self.engine_capacity = engine_capacity

class Bicycle(NonMotorized):
    def __init__(self, id, brand, model, type, gear_count, license_plate=None):
        super().__init__(id, license_plate, brand, model, type)
        self.gear_count = gear_count


# Added Vehicles / Objects
Car_1 = Car(1, "G12ass3AB", "Mercedes", "C-Class", "Petrol", 5, True)
Car_2 = Car(2, "W321B", "Opel", "Corsa", "Diesel", 3, False)

Cargo_truck = CargoTruck(1, "G11LKW", "MAN", "L123", "Diesel", "14000 Kg")

Motorbike = Motorcycle(1, "G10MTR", "Kawasaki", "Versys", "Petrol", 1000)

Bike = Bicycle(1, "Triban", "GRVL 120", "Manual", "16")


# Print specific details
print("---------------------------------")
print("Specific details are shown below:")
print()
print(f"Total Vehicles: {Vehicle.totalVehicles}")

print(f"Car1: ID:{Car_1.id}, {Car_1.brand}, Doors: {Car_1.number_of_doors}, Air Conditioning: {Car_1.air_conditioning}")
print(f"Car2: ID:{Car_2.id}, {Car_2.brand}, Doors: {Car_2.number_of_doors}, Air Conditioning: {Car_2.air_conditioning}")

print(f"CargoTruck: {Cargo_truck.brand}, Load Capacity: {Cargo_truck.load_capacity}")

print(f"Motorcycle: {Motorbike.brand}, Engine Capacity: {Motorbike.engine_capacity}")

print(f"Bicycle: {Bike.brand}, Gears: {Bike.gear_count}, Type: {Bike.type}, License Plate: {Bike.license_plate if Bike.license_plate else 'N/A'}")

print("---------------------------------")

print("Function outputs are shown below:")
print()
print(Vehicle.general_usage())
print()
print(Vehicle.show_totalVehicles())
print()
print(Car_1.drive())
print(Car_2.drive())
print()
print(Car_1.refuel())
print(Car_2.refuel())
print()
print(Cargo_truck.refuel())
print()
print(Bike.maintain())
print()
print(Cargo_truck.maintain())

print("---------------------------------")