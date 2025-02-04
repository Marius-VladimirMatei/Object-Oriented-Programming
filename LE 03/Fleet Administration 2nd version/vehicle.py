
# class for Vehicles

class Vehicle():
    totalVehicles = 0  # Class attribute that tracks the total number of vehicles

    # def __init__ constructor to initialize the attributes
    def __init__(self, id, brand, model, year):

        self.id = id
        self.brand = brand
        self.model = model
        self.year = year

        Vehicle.totalVehicles += 1  # Increment total vehicles when a new vehicle is created


