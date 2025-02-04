from vehicle import Vehicle
from motoritzed import Motorized
from non_motorized import NonMotorized
from car import Car
from cargo_truck import Cargo_truck
from motorcycle import Motorcycle
from bicycle import Bicycle
from vehicle_data_base import Vehicle_Data_Base




if __name__ == "__main__":
    data_base = Vehicle_Data_Base("vehicles.txt")

    car_1 = Car(
                1,
                "G123AB",
                "Ford",
                "Mondeo",
                "2024",
                5000,
                "Petrol",
                55,
                5
                )

    cargo_truck_1 = Cargo_truck(
        2,
        "CA123NA",
        "Mercedes",
        "Actros",
        2022,
        525000,
        "Diesel",
        450,
        2500,
        12000
    )

    data_base.add_vehicle(car_1)
    data_base.add_vehicle(cargo_truck_1)

    data_base.list_vehicles()
    data_base.save_vehicle()



car_1.refuel(55)

cargo_truck_1.load(7950)

cargo_truck_1.unload(950)











