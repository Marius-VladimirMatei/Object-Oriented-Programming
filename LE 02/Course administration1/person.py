import re


class Person:
    def __init__(self, name, address, post_code, telephone, email):
        # Ensure all arguments are strings
        if not all(isinstance(arg, str) for arg in [name, address, post_code, telephone, email]):
            raise TypeError("Please insert valid entries for name, address, post code, telephone, and email.")

        # Validate each attribute
        self.name = self.validate_name(name)
        self.address = self.validate_address(address)
        self.post_code = post_code
        self.telephone = self.validate_phone(telephone)
        self.email = self.validate_email(email)

    @staticmethod
    def validate_name(name):
        if re.match(r"^[äÄöÖüÜßA-Za-z\s]+$", name):
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
    def validate_post_code(post_code):
        pattern = r"^\d{4}$"
        if re.match(pattern, post_code):
            return post_code
        else:
            raise ValueError(f"Invalid email post_code: {post_code}")

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

    # Return a string representation that includes class's details
    def __str__(self):
        return f"Name: {self.name}, Address: {self.address}, Telephone: {self.telephone}, Email: {self.email}"

