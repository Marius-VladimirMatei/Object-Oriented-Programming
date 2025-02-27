from src.controllers.customer_controller import CustomerController
from src.controllers.vehicle_controller import VehicleController
from src.controllers.rental_controller import RentalController
from src.controllers.menu_controller import MenuController


def main():
    # Initialize controllers
    customer_controller = CustomerController()
    vehicle_controller = VehicleController()
    rental_controller = RentalController(vehicle_controller)

    # Create and run menu controller
    menu_controller = MenuController(
        customer_controller, vehicle_controller, rental_controller
    )
    menu_controller.run()


if __name__ == "__main__":
    main()
