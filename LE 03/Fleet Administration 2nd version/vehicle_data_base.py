from vehicle import Vehicle
from motorized import Motorized
from non_motorized import NonMotorized
from car import Car
from cargo_truck import Cargo_truck
from motorcycle import Motorcycle
from bicycle import Bicycle


# Data Base class to manage all the vehicle objects

class Vehicle_Data_Base:
    def __init__(self, filename="vehicles.txt"):
        self.vehicles = []  # List to store vehicle objects
        self.filename = filename

# add objects in list
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle.id} ({vehicle.brand} {vehicle.model}) added successfully.")

# save objects in txt file
    def save_vehicle(self):
        with open(self.filename, "w") as file:
            for vehicle in self.vehicles:
                if isinstance(vehicle, Motorized):
                    file.write(
                        f"ID: {vehicle.id}, "
                        f"License plate: {vehicle.license_plate}, "
                        f"Brand: {vehicle.brand}, "
                        f"Model: {vehicle.model}, "
                        f"Year: {vehicle.year}, "
                        f"Mileage: {vehicle.mileage}, "
                        f"Fuel type: {vehicle.fuel_type}, "
                        f"Fuel level: {vehicle.fuel_level} liters\n")

                elif isinstance(vehicle, Bicycle):  # Save Bicycle-specific attributes
                    file.write(
                        f"ID: {vehicle.id}, "
                        f"Brand: {vehicle.brand}, "
                        f"Model: {vehicle.model}, "
                        f"Year: {vehicle.year}, "
                        f"Type: {vehicle.type}, "
                        f"Gear count: {vehicle.gear_count}\n")

                elif isinstance(vehicle, NonMotorized):
                    file.write(
                        f"ID: {vehicle.id}, "
                        f"Brand: {vehicle.brand}, "
                        f"Model: {vehicle.model}, "
                        f"Year: {vehicle.year}, "
                        f"Type: {vehicle.type}\n")
        print("Vehicles saved successfully.")


# list all objects
    def list_vehicles(self):
        print("Vehicle list:")
        for vehicle in self.vehicles:
            if isinstance(vehicle, Cargo_truck):  # Display all cargo truck attributes
                print(f"ID: {vehicle.id}, "
                      f"License Plate: {vehicle.license_plate}, "
                      f"Brand: {vehicle.brand}, "
                      f"Model: {vehicle.model}, "
                      f"Year: {vehicle.year}, "
                      f"Mileage: {vehicle.mileage}, "
                      f"Fuel type: {vehicle.fuel_type}, "
                      f"Fuel level: {vehicle.fuel_level} liters, "
                      f"Current load: {vehicle.current_load} kg, "
                      f"Max load: {vehicle.max_load} kg")

            elif isinstance(vehicle, Motorized):  # Generic Motorized vehicles
                print(f"ID: {vehicle.id}, "
                      f"License Plate: {vehicle.license_plate}, "
                      f"Brand: {vehicle.brand}, "
                      f"Model: {vehicle.model}, "
                      f"Year: {vehicle.year}, "
                      f"Mileage: {vehicle.mileage}, "
                      f"Fuel type: {vehicle.fuel_type}, "
                      f"Fuel level: {vehicle.fuel_level} liters")

            elif isinstance(vehicle, Bicycle):
                print(f"ID: {vehicle.id}, "
                      f"Brand: {vehicle.brand}, "
                      f"Model: {vehicle.model}, "
                      f"Year: {vehicle.year}, "
                      f"Type: {vehicle.type}, "
                      f"Gear Count: {vehicle.gear_count}")

            elif isinstance(vehicle, NonMotorized):
                print(f"ID: {vehicle.id}, "
                      f"Brand: {vehicle.brand}, "
                      f"Model: {vehicle.model}, "
                      f"Year: {vehicle.year}, "
                      f"Type: {vehicle.type}")

# list only car objects
    def list_cars(self):
        print("Car list:")
        for vehicle in self.vehicles:
            if isinstance(vehicle, Car):
                print(f"ID: {vehicle.id}, "
                      f"License Plate: {vehicle.license_plate}, "
                      f"Brand: {vehicle.brand}, "
                      f"Model: {vehicle.model}, "
                      f"Year: {vehicle.year}, "
                      f"Mileage: {vehicle.mileage}, "
                      f"Fuel type: {vehicle.fuel_type}, "
                      f"Fuel level: {vehicle.fuel_level} liters\n")

# list only cargo objects
    def list_cargo_trucks(self):
        print("Cargo Truck list:")
        for vehicle in self.vehicles:
            if isinstance(vehicle, Cargo_truck):
                print(f"ID: {vehicle.id}, "
                      f"License Plate: {vehicle.license_plate}, "
                      f"Brand: {vehicle.brand}, "
                      f"Model: {vehicle.model}, "
                      f"Year: {vehicle.year}, "
                      f"Mileage: {vehicle.mileage}, "
                      f"Fuel type: {vehicle.fuel_type}, "
                      f"Fuel level: {vehicle.fuel_level} liters, "
                      f"Current load: {vehicle.current_load} kg,"
                      f"Max load: {vehicle.max_load} kg\n")

# list only moto objects
    def list_motorcycles(self):
        print("Motorcycle list:")
        for vehicle in self.vehicles:
            if isinstance(vehicle, Motorcycle):
                print(f"ID: {vehicle.id}, "
                      f"License Plate: {vehicle.license_plate}, "
                      f"Brand: {vehicle.brand}, "
                      f"Model: {vehicle.model}, "
                      f"Year: {vehicle.year}, "
                      f"Mileage: {vehicle.mileage}, "
                      f"Fuel type: {vehicle.fuel_type}, "
                      f"Fuel level: {vehicle.fuel_level} liters\n")

# list only bicycle objects
    def list_bicycles(self):
        print("Bicycle list:")
        for vehicle in self.vehicles:
            if isinstance(vehicle, Bicycle):
                print(f"ID: {vehicle.id}, "
                      f"Brand: {vehicle.brand}, "
                      f"Model: {vehicle.model}, "
                      f"Year: {vehicle.year}, "
                      f"Type: {vehicle.type}, "
                      f"Gear Count: {vehicle.gear_count}\n")
