from datetime import datetime
from src.models.rental_transaction import RentalTransaction
from src.utils.validator import Validator
import src.persistence.rental_storage as rental_storage


class RentalController:
    def __init__(self, vehicle_controller, storage_file="rentals.json"):
        self.storage_file = storage_file
        self.rentals = rental_storage.load_rentals(self.storage_file)
        self.vehicle_controller = vehicle_controller

    def get_next_id(self):
        # Get the highest rental ID and increment by 1
        if not self.rentals:
            return 1
        return max(rental.id for rental in self.rentals) + 1

    def create_rental(
        self, customer_id, vehicle_id, start_date, end_date, rental_id=None
    ):
        # Validate and assign rental ID
        if rental_id is None or rental_id == "":
            rental_id = self.get_next_id()
        else:
            rental_id = Validator.validate_id(rental_id)

        # Validate IDs
        customer_id = Validator.validate_id(customer_id)
        vehicle_id = Validator.validate_id(vehicle_id)

        # Validate dates using the Validator (expecting DD-MM-YYYY format)
        start_date, end_date = Validator.validate_rental_dates(start_date, end_date)

        # Check if the vehicle is available
        vehicle = next(
            (v for v in self.vehicle_controller.vehicles if v.id == vehicle_id), None
        )
        if vehicle is None:
            raise ValueError("Vehicle not found")
        if vehicle.status != "available":
            raise ValueError("Vehicle is already rented")

        # Create the rental transaction
        rental = RentalTransaction(
            rental_id, customer_id, vehicle_id, start_date, end_date
        )
        self.rentals.append(rental)
        rental_storage.save_rentals(self.rentals, self.storage_file)

        # Update the vehicle's status to "rented"
        self.vehicle_controller.update_vehicle_status(vehicle_id, "rented")
        return rental

    def return_vehicle(self, transaction_id):
        try:
            transaction_id = Validator.validate_id(transaction_id)

            for rental in self.rentals:
                if rental.id == transaction_id and rental.is_active():
                    # Format today's date in DD-MM-YYYY format
                    rental.return_date = datetime.now().strftime("%d-%m-%Y")

                    # Update the vehicle's status back to "available"
                    self.vehicle_controller.update_vehicle_status(
                        rental.vehicle_id, "available"
                    )
                    rental_storage.save_rentals(self.rentals, self.storage_file)
                    return True
            return False
        except ValueError:
            return False

    def list_active_rentals(self):
        active_rentals = [r for r in self.rentals if r.is_active()]
        for rental in active_rentals:
            print(rental)
