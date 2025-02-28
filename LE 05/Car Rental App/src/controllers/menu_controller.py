class MenuController:
    def __init__(self, customer_controller, vehicle_controller, rental_controller):
        self.customer_controller = customer_controller
        self.vehicle_controller = vehicle_controller
        self.rental_controller = rental_controller

    def display_menu(self):
        print("\n==== Vehicle Rental System ====")
        print("1. Add Vehicle")
        print("2. List Vehicles")
        print("3. Add Customer")
        print("4. List Customers")
        print("5. Create New Rental")
        print("6. Return Vehicle")
        print("7. List Active Rentals")
        print("8. Exit")

    def handle_add_vehicle(self):
        make = input("Enter Vehicle Make: ")
        model = input("Enter Vehicle Model: ")
        year = input("Enter Vehicle Year: ")
        try:
            vehicle = self.vehicle_controller.add_vehicle(make, model, year)
            print("\nVehicle added successfully!")
            print(vehicle)
        except ValueError as e:
            print(f"Error adding vehicle: {e}")

    def handle_list_vehicles(self):
        print("\nList of Vehicles:")
        self.vehicle_controller.list_vehicles()

    def handle_add_customer(self):
        name = input("Enter Customer Name: ")
        email = input("Enter Customer Email: ")
        telephone = input("Enter Customer Telephone: ")
        address = input("Enter Customer Address: ")
        try:
            customer = self.customer_controller.add_customer(
                name, email, telephone, address
            )
            print("\nCustomer added successfully!")
            print(customer)
        except ValueError as e:
            print(f"Error adding customer: {e}")

    def handle_list_customers(self):
        print("\nList of Customers:")
        self.customer_controller.list_customers()

    def handle_create_rental(self):
        print("\nCreate New Rental:")
        customer_id = input("Enter Customer ID: ")
        vehicle_id = input("Enter Vehicle ID: ")
        start_date = input("Enter Start Date (DD-MM-YYYY): ")
        end_date = input("Enter End Date (DD-MM-YYYY): ")
        try:
            rental = self.rental_controller.create_rental(
                customer_id, vehicle_id, start_date, end_date
            )
            print("\nRental created successfully!")
            print(rental)
        except ValueError as e:
            print(f"Error creating rental: {e}")

    def handle_return_vehicle(self):
        transaction_id = input("Enter Rental Transaction ID to return: ")
        try:
            transaction_id = int(transaction_id)
            if self.rental_controller.return_vehicle(transaction_id):
                print("Vehicle returned successfully!")
            else:
                print("Rental transaction not found or vehicle already returned.")
        except ValueError as e:
            print(f"Error processing return: {e}")

    def handle_list_active_rentals(self):
        print("\nActive Rentals:")
        active_rentals = [r for r in self.rental_controller.rentals if r.is_active()]
        if active_rentals:
            for rental in active_rentals:
                print(rental)
        else:
            print("No active rentals.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option: ")

            if choice == "1":
                self.handle_add_vehicle()
            elif choice == "2":
                self.handle_list_vehicles()
            elif choice == "3":
                self.handle_add_customer()
            elif choice == "4":
                self.handle_list_customers()
            elif choice == "5":
                self.handle_create_rental()
            elif choice == "6":
                self.handle_return_vehicle()
            elif choice == "7":
                self.handle_list_active_rentals()
            elif choice == "8":
                print("Exiting application.")
                break
            else:
                print("Invalid option. Please try again.")
