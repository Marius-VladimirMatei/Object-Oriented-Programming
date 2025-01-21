
class Vehicle:
    totalVehicles = 0 # Class attribute to track total number of vehicles

    def __init__(self, id, license_plate, brand, model, fuel_type):
        self.id = id
        self.licensePlate = license_plate
        self.brand = brand
        self.model = model
        self.fuelType = fuel_type


class Car(Vehicle):
    def __init__(self, id, license_plate, brand, model, fuel_type, number_of_doors, has_air_conditioning):
        # Initialize attributes of the parent class (Vehicle)
        super().__init__(id, license_plate, brand, model, fuel_type)
        # Initialize additional attributes specific to Car
        self.numberOfDoors = number_of_doors
        self.hasAirConditioning = has_air_conditioning


class Truck(Vehicle):
    def __init__(self, id, license_plate, brand, model, fuel_type, load_capacity):
        super().__init__(id, license_plate, brand, model, fuel_type)
        self.loadCapacity = load_capacity
        self.currentLoad = 0


class Motorcycle(Vehicle):
    def __init__(self, id, license_plate, brand, model, fuel_type, engine_capacity):
        super().__init__(id, license_plate, brand, model, fuel_type)
        self.engineCapacity = engine_capacity
        self.hasSidecar = False


class Bicycle(Vehicle):
    def __init__(self, id, license_plate, brand, model, fuel_type, type, gear_count):
        super().__init__(id, license_plate, brand, model, fuel_type)
        self.type = type
        self.gearCount = gear_count
