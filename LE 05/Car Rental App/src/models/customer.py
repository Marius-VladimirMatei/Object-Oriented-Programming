class Customer:
    def __init__(self, customer_id, name, email, telephone, address):
        self.id = customer_id
        self.name = name
        self.email = email
        self.telephone = telephone
        self.address = address

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "telephone": self.telephone,
            "address": self.address,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"], data["name"], data["email"], data["telephone"], data["address"]
        )

    def __str__(self):
        return f"Customer ID: {self.id}, Name: {self.name}, Email: {self.email}"
