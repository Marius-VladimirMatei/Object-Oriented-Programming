from vehicle import Vehicle
from motoritzed import Motorized
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

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle.id} ({vehicle.brand} {vehicle.model}) added successfully.")

    def save_vehicle(self):
        with open(self.filename, "w") as file:
            for vehicle in self.vehicles:
                if isinstance(vehicle, Motorized):
                    file.write(
                        f"{vehicle.id},"
                        f"{vehicle.license_plate},"
                        f"{vehicle.brand},"
                        f"{vehicle.model},"
                        f"{vehicle.year},"
                        f"{vehicle.mileage},"
                        f"{vehicle.fuel_type},"
                        f"{vehicle.fuel_level}\n")

                elif isinstance(vehicle, Bicycle):  # Save Bicycle-specific attributes
                    file.write(
                        f"{vehicle.id},"
                        f"{vehicle.brand},"
                        f"{vehicle.model},"
                        f"{vehicle.year},"
                        f"{vehicle.type},"
                        f"{vehicle.gear_count}\n")

                elif isinstance(vehicle, NonMotorized):
                    file.write(
                        f"{vehicle.id},"
                        f"{vehicle.brand},"
                        f"{vehicle.model},"
                        f"{vehicle.year},"
                        f"{vehicle.type}\n")
        print("Vehicles saved successfully.")

    def list_vehicles(self):
        print("Vehicle list:")
        for vehicle in self.vehicles:
            if isinstance(vehicle, Motorized):
                print(f"ID: {vehicle.id}, "
                      f"License Plate: {vehicle.license_plate}, "
                      f"Brand: {vehicle.brand}, "
                      f"Model: {vehicle.model}, "
                      f"Year: {vehicle.year}, "
                      f"Mileage: {vehicle.mileage}, "
                      f"Fuel type: {vehicle.fuel_type}, "
                      f"Fuel level: {vehicle.fuel_level}")

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



