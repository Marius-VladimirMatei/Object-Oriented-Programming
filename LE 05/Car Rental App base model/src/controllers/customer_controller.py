from src.models.customer import Customer
from src.utils.validator import Validator
from src.persistence.storage import Storage


class CustomerController:
    def __init__(self, storage_file="customers.json"):
        self.storage_file = storage_file
        self.storage: Storage[Customer] = Storage(self.storage_file, Customer)

    def get_next_id(self):
        # Get the highest customer ID and increment by 1
        if not self.storage.data:
            return 1
        return max(customer.id for customer in self.storage.data) + 1

    def add_customer(self, name, email, telephone, address, customer_id=None):
        # Auto-assign ID if not provided or empty
        if customer_id is None or customer_id == "":
            customer_id = self.get_next_id()
        else:
            customer_id = Validator.validate_id(customer_id)

        name = Validator.validate_name(name)
        email = Validator.validate_email(email)
        telephone = Validator.validate_telephone(telephone)
        address = Validator.validate_address(address)

        customer = Customer(customer_id, name, email, telephone, address)
        self.storage.data.append(customer)
        self.storage.save_data()
        return customer

    def list_customers(self):
        for customer in self.storage.data:
            print(customer)
