from motorized import Motorized

# class for Car objects

class Car(Motorized):
    def __init__(self, id, license_plate, brand, model, year, mileage, fuel_type, fuel_level, number_of_doors):
        super().__init__(id, license_plate, brand, model, year, mileage, fuel_type, fuel_level)
        self.number_of_doors = number_of_doors






