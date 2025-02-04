# class Person

class Person:
    def __init__(self, full_name, address, email, telephone_number, date_of_birth):
        self.full_name = full_name
        self.address = address
        self.email = email
        self.telephone_number = telephone_number
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"Name: {self.full_name}, Address: {self.address}, Email: {self.email}, Telephone: {self.telephone_number}, Date of birth: {self.date_of_birth}"
