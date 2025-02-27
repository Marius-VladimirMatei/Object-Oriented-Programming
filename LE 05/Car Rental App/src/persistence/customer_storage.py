import json
from src.models.customer import Customer


def save_customers(customers, storage_file="customers.json"):
    with open(storage_file, "w") as f:
        json.dump([customer.to_dict() for customer in customers], f, indent=4)


def load_customers(storage_file="customers.json"):
    try:
        with open(storage_file, "r") as f:
            data = json.load(f)
        return [Customer.from_dict(item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
