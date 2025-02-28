class Vehicle:
    def __init__(self, vehicle_id, make, model, year, status="available"):
        self.id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.status = status  # New attribute for vehicle availability

    def to_dict(self):
        return {
            "id": self.id,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data):
        # Default status to "available" if not provided
        return cls(
            data["id"],
            data["make"],
            data["model"],
            data["year"],
            data.get("status", "available"),
        )

    def __str__(self):
        return f"Vehicle ID: {self.id}, {self.year} {self.make} {self.model}, Status: {self.status}"
