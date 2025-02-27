import json
from src.models.vehicle import Vehicle


def save_vehicles(vehicles, storage_file="vehicles.json"):
    with open(storage_file, "w") as f:
        json.dump([vehicle.to_dict() for vehicle in vehicles], f, indent=4)


def load_vehicles(storage_file="vehicles.json"):
    try:
        with open(storage_file, "r") as f:
            data = json.load(f)
        return [Vehicle.from_dict(item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
