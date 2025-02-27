from src.models.vehicle import Vehicle
from src.utils.validator import Validator
import src.persistence.vehicle_storage as vehicle_storage


class VehicleController:
    def __init__(self, storage_file="vehicles.json"):
        self.storage_file = storage_file
        self.vehicles = vehicle_storage.load_vehicles(self.storage_file)

    def get_next_id(self):
        # Get the highest vehicle ID and increment by 1
        if not self.vehicles:
            return 1
        return max(vehicle.id for vehicle in self.vehicles) + 1

    def get_next_id(self):
        # Get the highest vehicle ID and increment by 1
        if not self.vehicles:
            return 1
        return max(vehicle.id for vehicle in self.vehicles) + 1

    def add_vehicle(self, make, model, year, vehicle_id=None):
        # Validate and assign vehicle ID
        if vehicle_id is None or vehicle_id == "":
            vehicle_id = self.get_next_id()
        else:
            vehicle_id = Validator.validate_id(vehicle_id)

        # Validate and sanitize inputs
        make = Validator.validate_string(make)
        model = Validator.validate_string(model)
        year = Validator.validate_year(year)

        # Create the vehicle object and persist it
        vehicle = Vehicle(vehicle_id, make, model, year)
        self.vehicles.append(vehicle)
        vehicle_storage.save_vehicles(self.vehicles, self.storage_file)
        return vehicle

    def list_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle)

    def update_vehicle_status(self, vehicle_id, new_status):
        # Update the status of a vehicle and persist the change
        for vehicle in self.vehicles:
            if vehicle.id == vehicle_id:
                vehicle.status = new_status
                vehicle_storage.save_vehicles(self.vehicles, self.storage_file)
                return True
        return False
