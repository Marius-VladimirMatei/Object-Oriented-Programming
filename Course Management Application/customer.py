from person import Person

# class Customer

class Customer(Person):
    def __init__(self, full_name, address, email, telephone_number, date_of_birth, customer_id):
        super().__init__(full_name, address, email, telephone_number, date_of_birth)
        self.customer_id = customer_id

    def __str__(self):
        return f"{super().__str__()}, Customer ID: {self.customer_id}"