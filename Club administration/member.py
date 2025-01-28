import re
class Member:
    def __init__(self, member_id, name, address, telephone, email, join_date, membership_status):
        if not all(isinstance(arg, str) for arg in
                   [member_id, name, address, telephone, email, join_date, membership_status]):
            raise TypeError("All input arguments must be strings.")

        self.id = member_id
        self.name = self.validate_name(name)
        self.address = self.validate_address(address)
        self.telephone = self.validate_phone(telephone)
        self.email = self.validate_email(email)
        self.join_date = self.validate_date(join_date)
        self.membership_status = self.validate_membership_status(membership_status)

    @staticmethod
    def validate_name(name):
        if re.match(r"^[A-Za-z\s]+$", name):
            return name
        else:
            raise ValueError(f"Invalid name: {name}")

    @staticmethod
    def validate_address(address):
        if re.match(r"^[A-Za-z0-9\s,.-]+$", address):
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

    @staticmethod
    def validate_date(join_date):
        pattern = r"^\d{4}-\d{2}-\d{2}$"  # Format: YYYY-MM-DD
        if re.match(pattern, join_date):
            return join_date
        else:
            raise ValueError(f"Invalid date format: {join_date}")

    @staticmethod
    def validate_membership_status(membership_status):
        if membership_status in ["Active", "Inactive"]:
            return membership_status
        else:
            raise ValueError(f"Invalid membership status: {membership_status}")

    def pay_dues(self):
        print(f"Member: {self.name} has paid dues")

    def update_member_details(self, name=None, membership_status=None):
        if name:
            self.name = name
        if membership_status:
            self.membership_status = membership_status
        print(f"Updated details for {self.name}: Status - {self.membership_status}")

    def get_member_info(self):
        return f"Member INFO: ID: {self.id}, Name: {self.name}, Status: {self.membership_status}"
