from motorized import Motorized

# class for cargo_truck objects and specific methods


class Cargo_truck(Motorized):
    def __init__(self, id, license_plate, brand, model, year, mileage, fuel_type, fuel_level, current_load, max_load):
        super().__init__(id, license_plate, brand, model, year, mileage, fuel_type, fuel_level)
        self.current_load = current_load
        self.max_load = max_load

    def load(self, amount):
        if self.current_load + amount <= self.max_load:
            self.current_load += amount
            print(f"Truck ID {self.id} loaded {amount} kg. Current load: {self.current_load} kg.")
        else:
            print("Cannot load beyond maximum capacity.")

    def unload(self, amount):
        if amount <= self.current_load:
            self.current_load -= amount
            print(f"Truck ID {self.id} unloaded {amount} kg. Current load: {self.current_load} kg.")
        else:
            print("Cannot unload more than the current load.")






