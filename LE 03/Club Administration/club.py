
from validator import Validator

class Club:
    def __init__(self, name: str, address: str, telephone_number: str, email_address: str):
        self.name = Validator.validate_name(name)
        self.address = Validator.validate_address(address)
        self.telephone_number = Validator.validate_telephone(telephone_number)
        self.email_address = Validator.validate_email(email_address)

