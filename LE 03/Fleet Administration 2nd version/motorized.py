from vehicle import Vehicle

# Class Motorized and specific methods

class Motorized(Vehicle):
    def __init__(self, id, license_plate, brand, model, year, mileage, fuel_type, fuel_level):

        super().__init__(id, brand, model, year)

        self.license_plate = license_plate
        self.mileage = mileage
        self.fuel_type = fuel_type
        self.fuel_level = fuel_level


    def update_mileage(self, new_mileage):
        if new_mileage > self.mileage:
            self.mileage = new_mileage
            print(f"Mileage updated to {self.mileage} km.")
        else:
            print("New mileage must be greater than the current mileage.")

    def refuel(self, amount):
        self.fuel_level += amount
        print(f"Vehicle ID {self.id} refueled {amount} litres. Current fuel level: {self.fuel_level} litres.")




