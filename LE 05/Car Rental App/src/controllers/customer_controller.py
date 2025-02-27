from src.models.customer import Customer
from src.utils.validator import Validator
import src.persistence.customer_storage as customer_storage


class CustomerController:
    def __init__(self, storage_file="customers.json"):
        self.storage_file = storage_file
        self.customers = customer_storage.load_customers(self.storage_file)

    def get_next_id(self):
        # Get the highest customer ID and increment by 1
        if not self.customers:
            return 1
        return max(customer.id for customer in self.customers) + 1

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
        self.customers.append(customer)
        customer_storage.save_customers(self.customers, self.storage_file)
        return customer

    def list_customers(self):
        for customer in self.customers:
            print(customer)

    def add_customer_ui(self):
        # Interactive UI method to collect customer information and add a customer
        try:
            name = input("Enter Customer Name: ")
            email = input("Enter Customer Email: ")
            telephone = input("Enter Customer Telephone: ")
            address = input("Enter Customer Address: ")

            # Auto-increment ID by passing None
            customer = self.add_customer(name, email, telephone, address)
            print(f"Customer added successfully!")
            print(customer)
            return customer
        except ValueError as e:
            print(f"Error: {e}")
            return None
