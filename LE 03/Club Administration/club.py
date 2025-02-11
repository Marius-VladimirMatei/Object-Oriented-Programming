
from validator import Validator

class Club:

    clubs = [] # class level list to store all clubs

    def __init__(self, name, address, telephone_number, email_address):
        self.name = Validator.validate_name(name)
        self.address = Validator.validate_address(address)
        self.telephone_number = Validator.validate_telephone(telephone_number)
        self.email_address = Validator.validate_email(email_address)

    # Creates a new Club instance, adds it to the class-level clubs list, and returns the instance.

    @classmethod
    def create_club(cls, name: str, address: str, telephone_number: str, email_address: str):

        club = cls(name, address, telephone_number, email_address)
        cls.clubs.append(club)
        return club

    # Returns the club details in a formatted string.
    def get_club_details(self):

        details = (
            f"Club Name: {self.name}\n"
            f"Address: {self.address}\n"
            f"Telephone: {self.telephone_number}\n"
            f"Email: {self.email_address}"
        )
        return details

