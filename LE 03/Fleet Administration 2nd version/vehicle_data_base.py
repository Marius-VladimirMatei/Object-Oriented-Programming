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


# load the txt file needed in GUI
    def load_vehicles(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    attributes = dict(attr.split(": ") for attr in line.strip().split(", "))

                    vehicle_id = int(attributes["ID"])
                    brand = attributes["Brand"]
                    model = attributes["Model"]
                    year = int(attributes["Year"])

                    if "License plate" in attributes:  # Motorized Vehicles
                        license_plate = attributes["License plate"]
                        mileage = int(attributes["Mileage"])
                        fuel_type = attributes["Fuel type"]
                        fuel_level = float(attributes["Fuel level"].split()[0])

                        if "Current load" in attributes:  # Cargo Truck
                            current_load = int(attributes["Current load"].split()[0])
                            max_load = int(attributes["Max load"].split()[0])
                            vehicle = Cargo_truck(vehicle_id, license_plate, brand, model, year, mileage, fuel_type,
                                                  fuel_level, current_load, max_load)

                        elif "Number of doors" in attributes:  # Car
                            number_of_doors = int(attributes["Number of doors"])
                            vehicle = Car(vehicle_id, license_plate, brand, model, year, mileage, fuel_type, fuel_level,
                                          number_of_doors)

                        else:  # Motorcycle
                            vehicle = Motorcycle(vehicle_id, license_plate, brand, model, year, mileage, fuel_type,
                                                 fuel_level)

                    elif "Gear count" in attributes:  # Bicycle
                        gear_count = int(attributes["Gear count"])
                        vehicle_type = attributes["Type"]
                        vehicle = Bicycle(vehicle_id, brand, model, year, vehicle_type, gear_count)

                    else:  # Non-Motorized
                        vehicle_type = attributes["Type"]
                        vehicle = NonMotorized(vehicle_id, brand, model, year, vehicle_type)

                    self.vehicles.append(vehicle)

            print("Vehicles loaded successfully.")

        except FileNotFoundError:
            print("No saved vehicle data found.")
        except Exception as e:
            print(f"Error loading vehicles: {e}")


    # list all objects
    def list_vehicles(self):

        vehicle_list = []
        print("Vehicle list:")

        for vehicle in self.vehicles:
            if isinstance(vehicle, Cargo_truck):  # Display all cargo truck attributes
                vehicle_info = (
                    f"ID: {vehicle.id}, License Plate: {vehicle.license_plate}, Brand: {vehicle.brand}, "
                    f"Model: {vehicle.model}, Year: {vehicle.year}, Mileage: {vehicle.mileage}, "
                    f"Fuel type: {vehicle.fuel_type}, Fuel level: {vehicle.fuel_level} liters, "
                    f"Current load: {vehicle.current_load} kg, Max load: {vehicle.max_load} kg"
                )

            elif isinstance(vehicle, Motorized):  # Generic Motorized vehicles
                vehicle_info = (
                    f"ID: {vehicle.id}, License Plate: {vehicle.license_plate}, Brand: {vehicle.brand}, "
                    f"Model: {vehicle.model}, Year: {vehicle.year}, Mileage: {vehicle.mileage}, "
                    f"Fuel type: {vehicle.fuel_type}, Fuel level: {vehicle.fuel_level} liters"
                )

            elif isinstance(vehicle, Bicycle):
                vehicle_info = (
                    f"ID: {vehicle.id}, Brand: {vehicle.brand}, Model: {vehicle.model}, Year: {vehicle.year}, "
                    f"Type: {vehicle.type}, Gear Count: {vehicle.gear_count}"
                )

            elif isinstance(vehicle, NonMotorized):
                vehicle_info = (
                    f"ID: {vehicle.id}, Brand: {vehicle.brand}, Model: {vehicle.model}, Year: {vehicle.year}, "
                    f"Type: {vehicle.type}"
                )

            print(vehicle_info)  #  Print to console
            vehicle_list.append(vehicle_info)  # Add to list for GUI

        return vehicle_list  # Returns formatted list for Listbox

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
