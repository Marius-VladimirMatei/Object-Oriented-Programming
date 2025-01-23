from abc import ABC, abstractmethod
from datetime import datetime


# Base Class for all Motorized and NonMotorized
class Vehicle(ABC):
    totalVehicles = 0  # Class attribute that tracks the total number of vehicles

    # def __init__ constructor to initialize the attributes
    def __init__(self, id, license_plate, brand, model):
        if not isinstance(id, int):
            raise ValueError("Id must be a positive number.")

        if license_plate is not None and not isinstance(license_plate, str):  # Allow None for license_plate
            raise ValueError("License plate, brand, and model must be text.")

        if not isinstance(brand, str) or not isinstance(model, str):
            raise ValueError("Brand and model must be text.")

        self.id = id
        self.license_plate = license_plate
        self.brand = brand
        self.model = model

        Vehicle.totalVehicles += 1  # Increment total vehicles when a new vehicle is created

    @abstractmethod  # Abstract method to enforce implementation in subclasses.
    def drive(self):
        pass

    @abstractmethod  # Abstract method to enforce implementation in subclasses.
    def maintain(self):
        pass

    @staticmethod  # utility function decorator: the function does not require access to instance or self. parameter
    def show_totalVehicles():
        return f"There are {Vehicle.totalVehicles} vehicles."

    @staticmethod
    def general_usage():
        return "Vehicles are used to transport people or goods."


# Inherits from Vehicle. Is the Parent Class for Car, CargoTruck and Motorcycle
class Motorized(Vehicle):
    def __init__(self, id, license_plate, brand, model, fuel_type, mileage):
        # super().__init__ initializes the attributes from the Parent Class
        super().__init__(id, license_plate, brand, model)

        if not isinstance(fuel_type, str):
            raise ValueError("Fuel must be Petrol, Diesel or Electric.")

        if not isinstance(mileage, int) or mileage < 0:
            raise ValueError("Mileage must pe a positive number.")

        self.fuel_type = fuel_type
        self.current_mileage = mileage
        self.mileage = mileage

    def update_mileage(self, new_user_mileage):
        if not isinstance(new_user_mileage, int) or new_user_mileage < 0:
            raise ValueError("New mileage from user must be a positive number.")

        if self.current_mileage + new_user_mileage < self.mileage:
            raise ValueError("Error in adding mileage to vehicle.")
        self.current_mileage += new_user_mileage

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

        if not isinstance(type, str):
            raise ValueError("Type must be Manual or Electric.")

        self.type = type  # "manual" or "electric"

    def drive(self):
        return f"{self.brand} {self.model} {self.type} is powered by human effort."

    def maintain(self):
        return f"{self.brand} {self.model} {self.type} is being checked for wear and tear."


class Car(Motorized):
    def __init__(self, id, license_plate, brand, model, fuel_type, number_of_doors, has_air_conditioning, mileage):
        super().__init__(id, license_plate, brand, model, fuel_type, mileage)
        if not isinstance(number_of_doors, int) or number_of_doors < 2 or number_of_doors > 5:
            raise ValueError("Number of doors must be a number between 2 and 5.")

        self.number_of_doors = number_of_doors
        self.has_air_conditioning = bool(has_air_conditioning)


class CargoTruck(Motorized):
    def __init__(self, id, license_plate, brand, model, fuel_type, load_capacity, mileage):
        super().__init__(id, license_plate, brand, model, fuel_type, mileage)
        if not isinstance(load_capacity, (int, float)) or load_capacity < 0:
            raise ValueError("Load capacity must be a positive number.")

        self.load_capacity = load_capacity
        self.current_load = 0


class Motorcycle(Motorized):
    def __init__(self, id, license_plate, brand, model, fuel_type, engine_capacity, mileage):
        super().__init__(id, license_plate, brand, model, fuel_type, mileage)
        if not isinstance(engine_capacity, int) or engine_capacity < 0:
            raise ValueError("Engine capacity must be a positive number.")

        self.engine_capacity = engine_capacity


class Bicycle(NonMotorized):
    def __init__(self, id, brand, model, type, gear_count, license_plate=None):
        super().__init__(id, license_plate, brand, model, type)

        if not isinstance(gear_count, int) or gear_count < 1 or gear_count > 16:
            raise ValueError("Gear count must be between 1 and 16.")

        self.gear_count = gear_count


# Added Vehicles / Objects
Car_1 = Car(
    1,
    "G12ass3AB",
    "Mercedes",
    "C-Class",
    "Petrol",
    5,
    True,
    5000  # Mileage
)

Car_2 = Car(
    2,
    "W321B",
    "Opel",
    "Corsa",
    "Diesel",
    3,
    False,
    3000  # Mileage
)

Cargo_truck = CargoTruck(
    1,
    "G11LKW",
    "MAN",
    "L123",
    "Diesel",
    14000,  # Load capacity
    10000   # Mileage
)

Motorbike = Motorcycle(
    1,
    "G10MTR",
    "Kawasaki",
    "Versys",
    "Petrol",
    1000,  # Engine capacity
    2000   # Mileage
)

Bike = Bicycle(
    1,
    "Triban",  # Brand
    "GRVL 120",  # Model
    "Manual",  # Type
    16,  # Gear count
    None  # License plate (optional)
)

# Print specific details
print("---------------------------------")
print("Specific details are shown below:")
print()
print(f"Total Vehicles: {Vehicle.totalVehicles}")

print(
    f"Car1: ID:{Car_1.id}, {Car_1.brand}, Doors: {Car_1.number_of_doors}, Air Conditioning: {Car_1.has_air_conditioning}")
print(
    f"Car2: ID:{Car_2.id}, {Car_2.brand}, Doors: {Car_2.number_of_doors}, Air Conditioning: {Car_2.has_air_conditioning}")

print(f"CargoTruck: {Cargo_truck.brand}, Load Capacity: {Cargo_truck.load_capacity}")

print(f"Motorcycle: {Motorbike.brand}, Engine Capacity: {Motorbike.engine_capacity}")

print(
    f"Bicycle: {Bike.brand}, Gears: {Bike.gear_count}, Type: {Bike.type}, License Plate: {Bike.license_plate if Bike.license_plate else 'N/A'}")

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


# Updating mileage for Car_1
print(f"Initial mileage for Car_1: {Car_1.current_mileage}")
try:
    Car_1.update_mileage(1500)  # Add 1500 km to the current mileage
    print(f"Updated mileage for Car_1: {Car_1.current_mileage}")
except ValueError as e:
    print(f"Error updating mileage:")

# Updating mileage for Motorbike
print(f"Initial mileage for Motorbike: {Motorbike.current_mileage}")
try:
    Motorbike.update_mileage(300)  # Add 300 km to the current mileage
    print(f"Updated mileage for Motorbike: {Motorbike.current_mileage}")
except ValueError as e:
    print(f"Error updating mileage: {e}")