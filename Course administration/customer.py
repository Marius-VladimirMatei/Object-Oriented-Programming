import re
from person import Person

class Customer(Person):
    def __init__(self, name, address, telephone, email, customer_id):
        # Call the parent class's constructor
        super().__init__(name, address, telephone, email)

        # Validate the customer_id
        if not isinstance(customer_id, int) or not re.match(r"^\d{3}$", str(customer_id)):
            raise ValueError ("Customer ID must contain 3 digits.")

        self.customer_id = customer_id

    # Return a string representation that includes class's details
    def __str__(self):
        return f"{super().__str__()}, Customer ID: {self.customer_id}"


