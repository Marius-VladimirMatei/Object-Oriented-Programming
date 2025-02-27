from src.controllers.customer_controller import CustomerController
from src.controllers.vehicle_controller import VehicleController
from src.controllers.rental_controller import RentalController


def main():
    # Initialize controllers
    customer_controller = CustomerController()
    vehicle_controller = VehicleController()
    rental_controller = RentalController(vehicle_controller)

    while True:
        print("\n==== Vehicle Rental System ====")
        print("1. Add Vehicle")
        print("2. List Vehicles")
        print("3. Add Customer")
        print("4. List Customers")
        print("5. Create New Rental")
        print("6. Return Vehicle")
        print("7. List Active Rentals")
        print("8. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            # Add Vehicle
            make = input("Enter Vehicle Make: ")
            model = input("Enter Vehicle Model: ")
            year = input("Enter Vehicle Year: ")
            try:
                vehicle = vehicle_controller.add_vehicle(make, model, year)
                print("\nVehicle added successfully!")
                print(vehicle)
            except ValueError as e:
                print(f"Error adding vehicle: {e}")

        elif choice == "2":
            # List Vehicles
            print("\nList of Vehicles:")
            vehicle_controller.list_vehicles()

        elif choice == "3":
            # Add Customer
            name = input("Enter Customer Name: ")
            email = input("Enter Customer Email: ")
            telephone = input("Enter Customer Telephone: ")
            address = input("Enter Customer Address: ")
            try:
                customer = customer_controller.add_customer(
                    name, email, telephone, address
                )
                print("\nCustomer added successfully!")
                print(customer)
            except ValueError as e:
                print(f"Error adding customer: {e}")

        elif choice == "4":
            # List Customers
            print("\nList of Customers:")
            customer_controller.list_customers()

        elif choice == "5":
            # Create New Rental
            customer_id = input("Enter Customer ID: ")
            vehicle_id = input("Enter Vehicle ID: ")
            start_date = input("Enter Start Date (DD-MM-YYYY): ")
            end_date = input("Enter End Date (DD-MM-YYYY): ")
            try:
                rental = rental_controller.create_rental(
                    customer_id, vehicle_id, start_date, end_date
                )
                print("\nRental created successfully!")
                print(rental)
            except ValueError as e:
                print(f"Error creating rental: {e}")

        elif choice == "6":
            # Return Vehicle
            transaction_id = input("Enter Rental Transaction ID to return: ")
            try:
                transaction_id = int(transaction_id)
                if rental_controller.return_vehicle(transaction_id):
                    print("Vehicle returned successfully!")
                else:
                    print("Rental transaction not found or vehicle already returned.")
            except ValueError as e:
                print(f"Error processing return: {e}")

        elif choice == "7":
            # List Active Rentals
            print("\nActive Rentals:")
            active_rentals = [r for r in rental_controller.rentals if r.is_active()]
            if active_rentals:
                for rental in active_rentals:
                    print(rental)
            else:
                print("No active rentals.")

        elif choice == "8":
            print("Exiting application.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
