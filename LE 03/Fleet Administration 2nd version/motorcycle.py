from motorized import Motorized

# class for Motorcycle objects

class Motorcycle(Motorized):
    def __init__(self, id, license_plate, brand, model, year, mileage, fuel_type, fuel_level):
        super().__init__(id, license_plate, brand, model, year, mileage, fuel_type, fuel_level)

