import re

class Vehicle:
    total_vehicles = 0  # Class attribute to keep track of total vehicles

    def __init__(self, vehicle_id, brand, model, year, mileage, fuel_type=None, fuel_level=0):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_type = fuel_type
        self.fuel_level = fuel_level

        Vehicle.total_vehicles += 1

    def refuel(self, amount):
        """ Increase fuel level by specified amount. """
        if self.fuel_type:
            self.fuel_level += amount
            return f"Vehicle {self.vehicle_id} refueled with {amount}L. New level: {self.fuel_level}L"
        else:
            return f"Vehicle {self.vehicle_id} does not use fuel."

    def display_info(self):
        return f"{self.vehicle_id}: {self.brand} {self.model} ({self.year}) - Mileage: {self.mileage} km, Fuel: {self.fuel_level}L"

    @staticmethod
    def validate_id(vehicle_id):
        if re.match(r"^[A-Z0-9]+$", vehicle_id):
            return vehicle_id
        raise ValueError("Invalid Vehicle ID format.")

    @staticmethod
    def validate_string(value):
        if re.match(r"^[A-Za-z0-9\s]+$", value):
            return value
        raise ValueError("Invalid string format.")

    @staticmethod
    def validate_year(year):
        if isinstance(year, int) and 1900 <= year <= 2100:
            return year
        raise ValueError("Invalid year format.")

    @staticmethod
    def validate_mileage(mileage):
        if isinstance(mileage, (int, float)) and mileage >= 0:
            return mileage
        raise ValueError("Invalid mileage format.")

    def refuel(self, amount):
        if self.fuel_type:
            self.fuel_level += amount
        else:
            raise ValueError("This vehicle does not use fuel.")

    def display_info(self):
        return f"{self.vehicle_id}: {self.brand} {self.model} ({self.year}) - Mileage: {self.mileage} km, Fuel: {self.fuel_level}L"

class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, year, mileage, fuel_type, fuel_level, seating_capacity):
        super().__init__(vehicle_id, brand, model, year, mileage, fuel_type, fuel_level)
        self.seating_capacity = seating_capacity


class Truck(Vehicle):
    def __init__(self, vehicle_id, brand, model, year, mileage, fuel_type, fuel_level, current_cargo, max_load):
        super().__init__(vehicle_id, brand, model, year, mileage, fuel_type, fuel_level)
        self.current_cargo = current_cargo
        self.max_load = max_load

class Motorcycle(Vehicle):
    def __init__(self, vehicle_id, brand, model, year, mileage, fuel_type, fuel_level, engine_size):
        super().__init__(vehicle_id, brand, model, year, mileage, fuel_type, fuel_level)
        self.engine_size = engine_size

class Bicycle(Vehicle):
    def __init__(self, vehicle_id, brand, model, year, mileage):
        super().__init__(vehicle_id, brand, model, year, mileage)

