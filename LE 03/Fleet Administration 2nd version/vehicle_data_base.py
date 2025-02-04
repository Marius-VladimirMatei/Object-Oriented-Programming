
# Data Base class to manage all the vehicle objects

class Vehicle_Data_Base:
    def __init__(self, filename="vehicles.txt"):
        self.vehicles = []  # List to store vehicle objects
        self.filename = filename

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle.id} ({vehicle.brand} {vehicle.model}) added successfully.")


    def save_vehicle(self):
        with open(self.filename, "w") as file:
            for vehicle in self.vehicles:
                file.write(f"{vehicle.id},{vehicle.brand},{vehicle.model},{vehicle.year}\n")
        print(f"All vehicles saved to {self.filename} successfully.")


    def list_vehicles(self):
        if not self.vehicles:
            print("No vehicles in registry.")
        else:
            print("All vehicles")
            for vehicle in self.vehicles:
                print(f"ID: {vehicle.id}, License Plate: {vehicle.license_plate}, Brand: {vehicle.brand}, Model: {vehicle.model}, Year: {vehicle.year}, Mileage: {vehicle.mileage}, Fuel type: {vehicle.fuel_type}, Fuel level: {vehicle.fuel_level}")


