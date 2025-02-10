import json
from validator import Validator


class Member:
    def __init__(self, id, name, address, telephone_number, email_address, join_date, membership_status):
        # Validate and set attributes
        self.id = int(Validator.validate_numeric(str(id)))
        self.name = Validator.validate_name(name)
        self.address = Validator.validate_address(address)
        self.telephone_number = Validator.validate_telephone(telephone_number)
        self.email_address = Validator.validate_email(email_address)
        self.join_date = Validator.validate_date(join_date)  # Expected format: DD/MM/YYYY
        self.membership_status = membership_status

    def to_dict(self):
        """Convert the Member instance into a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "telephone_number": self.telephone_number,
            "email_address": self.email_address,
            "join_date": self.join_date,
            "membership_status": self.membership_status
        }






