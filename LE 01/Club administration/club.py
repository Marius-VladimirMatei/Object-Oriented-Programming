import re
# Class and methods

class Club:
    _total_members = 0  # Class variable to count total number of members

    def __init__(self, name, address, telephone, email):
        if not isinstance(name, str) or not isinstance(address, str) or not isinstance(telephone, str) or not isinstance(email, str):
            raise ValueError("Name, address, telephone, and email must be strings")

        self.name = self.validate_name(name)
        self.address = self.validate_address(address)
        self.telephone = self.validate_phone(telephone)
        self.email = self.validate_email(email)
        self.members = []  # List to hold the members

    @staticmethod
    def validate_name(name):
        if re.match(r"^[ÖöÜüßÄäA-Za-z\s]+$", name):
            return name
        else:
            raise ValueError(f"Invalid name: {name}")

    @staticmethod
    def validate_address(address):
        if re.match(r"^[ÖöÜüßÄäA-Za-z0-9\s,.-]+$", address):
            return address
        else:
            raise ValueError(f"Invalid address: {address}")

    @staticmethod
    def validate_phone(telephone):
        pattern = r"^\+?\d{1,4}?[-.\s]?\(?\d+\)?[-.\s]?\d{1,5}[-.\s]?\d{1,5}[-.\s]?\d{1,5}$"
        if re.match(pattern, telephone):
            return telephone
        else:
            raise ValueError(f"Invalid phone number: {telephone}")

    @staticmethod
    def validate_email(email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(pattern, email):
            return email
        else:
            raise ValueError(f"Invalid email address: {email}")

    @classmethod
    def get_total_members(cls):
        return cls._total_members

    def add_member(self, member):
        self.members.append(member)
        Club._total_members += 1  # Increment member count when a new member is added
        print(f"Added member: {member.name}")  # Print the name of the member

    def remove_member(self, id):
        self.members = [m for m in self.members if m.id != id]
        Club._total_members -= 1  # Decrement member count when a member is removed
        print(f"Member removed")

    def get_club_details(self):
        return f"Club DETAILS: Name: {self.name}, Address: {self.address}, Phone: {self.telephone}, Email: {self.email}"