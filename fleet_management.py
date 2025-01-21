
# Base Class for all Motorized and NonMotorized
class Vehicle:
    totalVehicles = 0 # Class attribute that tracks the total number of vehicles

    # def __init__ constructor to initialize the attributes
    def __init__(self, id, license_plate, brand, model):
        self.id = id
        self.license_plate = license_plate
        self.brand = brand
        self.model = model

        Vehicle.totalVehicles +=1 # Increment total vehicles when a new vehicle is created


# Inherits from Vehicle. Is the Parent Class for Car, CargoTruck and Motorcycle
class Motorized(Vehicle):
    def __init__(self, id, license_plate, brand, model, fuel_type):
        # super().__init__ initializes the attributes form the Parent Class
        super().__init__(id, license_plate, brand, model)
        self.fuel_type = fuel_type


# Inherits from Vehicle. Is the Parent Class for Bicycle
class NonMotorized(Vehicle):
    def __init__(self, id, license_plate, brand, model, type):
        super().__init__(id, license_plate, brand, model)
        self.type = type # "manual" or "electric"


class Car(Motorized):
    def __init__(self, id, license_plate, brand, model, fuel_type, doors_number, air_conditioning):
        super().__init__(id, license_plate, brand, model, fuel_type)
        self.doors_number = doors_number
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


# Added Vehicles
Car_1 = Car(1, "G123AB", "Mercedes", "C-Class", "Petrol", 5, True)
Car_2 = Car(2, "W321B", "Opel", "Corsa", "Diesel", 3, False)

Cargo_truck = CargoTruck(1, "G11LKW", "MAN", "L123", "Diesel", "14000 Kg")

Motorbike = Motorcycle(1, "G10MTR", "Kawasaki", "Versys", "Petrol", 1000)

Bike = Bicycle(1, "Triban", "GRVL 120", "Manual", "16")


# Print specific details
print(f"Total Vehicles: {Vehicle.totalVehicles}")

print(f"Car1: ID:{Car_1.id}, {Car_1.brand}, Doors: {Car_1.doors_number}, Air Conditioning: {Car_1.air_conditioning}")
print(f"Car2: ID:{Car_2.id}, {Car_2.brand}, Doors: {Car_2.doors_number}, Air Conditioning: {Car_2.air_conditioning}")

print(f"CargoTruck: {Cargo_truck.brand}, Load Capacity: {Cargo_truck.load_capacity}")

print(f"Motorcycle: {Motorbike.brand}, Engine Capacity: {Motorbike.engine_capacity}")

print(f"Bicycle: {Bike.brand}, Gears: {Bike.gear_count}, Type: {Bike.type}, License Plate: {Bike.license_plate if Bike.license_plate else 'N/A'}")