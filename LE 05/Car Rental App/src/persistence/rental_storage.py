import json
from src.models.rental_transaction import RentalTransaction


def save_rentals(rentals, storage_file="rentals.json"):
    with open(storage_file, "w") as f:
        json.dump([rental.to_dict() for rental in rentals], f, indent=4)


def load_rentals(storage_file="rentals.json"):
    try:
        with open(storage_file, "r") as f:
            data = json.load(f)
        return [RentalTransaction.from_dict(item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
