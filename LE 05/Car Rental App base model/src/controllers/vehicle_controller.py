from src.models.vehicle import Vehicle
from src.utils.validator import Validator
from src.persistence.storage import Storage


class VehicleController:
    def __init__(self, storage_file="vehicles.json"):
        self.storage_file = storage_file

        # Storage[Vehicle] is a specific type of Storage that stores Vehicle objects
        self.storage: Storage[Vehicle] = Storage(self.storage_file, Vehicle)

    def get_next_id(self):
        # Get the highest vehicle ID and increment by 1
        if not self.storage.data:
            return 1
        return max(vehicle.id for vehicle in self.storage.data) + 1

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
        self.storage.data.append(vehicle)
        self.storage.save_data()
        return vehicle

    def list_vehicles(self):
        for vehicle in self.storage.data:
            print(vehicle)

    def update_vehicle_status(self, vehicle_id, new_status):
        # Update the status of a vehicle and persist the change
        for vehicle in self.storage.data:
            if vehicle.id == vehicle_id:
                vehicle.status = new_status
                self.storage.save_data()
                return True
        return False
