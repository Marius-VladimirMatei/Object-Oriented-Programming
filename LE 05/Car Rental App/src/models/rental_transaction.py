from datetime import datetime


class RentalTransaction:
    def __init__(self, rental_id, customer_id, vehicle_id, start_date, end_date):
        self.id = rental_id
        self.customer_id = customer_id
        self.vehicle_id = vehicle_id
        self.start_date = start_date
        self.end_date = end_date
        self.return_date = None

    def is_active(self):
        return self.return_date is None

    def to_dict(self):
        # Convert transaction to dictionary for storage
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "vehicle_id": self.vehicle_id,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "return_date": self.return_date,
        }

    @classmethod
    def from_dict(cls, data):
        # Create transaction object from dictionary
        transaction = cls(
            data["id"],
            data["customer_id"],
            data["vehicle_id"],
            data["start_date"],
            data["end_date"],
        )
        if "return_date" in data:
            transaction.return_date = data["return_date"]
        return transaction

    def __str__(self):
        # String representation of the rental transaction
        status = (
            "Active" if self.return_date is None else f"Returned on {self.return_date}"
        )
        return f"Rental ID: {self.id}, Customer ID: {self.customer_id}, Vehicle ID: {self.vehicle_id}, Start Date: {self.start_date}, End Date: {self.end_date}, {status}"
