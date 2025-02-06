from vehicle import Vehicle
from motorized import Motorized
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

    bicycle_1 = Bicycle(
        102,
        "Bicycle brand",
        "Model",
        2023,
        "Bicycle",
        18
    )


    motorcycle_1 = Motorcycle(
        108,
        "License plate motorcycle",
        "BMW",
        "R1250",
        "2025",
        2500,
        "Petrol",
        15
    )


    print("Create objects-----")
    data_base.add_vehicle(motorcycle_1)

    data_base.add_vehicle(bicycle_1)

    data_base.add_vehicle(car_1)
    data_base.add_vehicle(cargo_truck_1)

    data_base.list_vehicles()
    data_base.save_vehicle()


    print("Refuel, load, unload-----")
    motorcycle_1.refuel(90)

    car_1.refuel(55)

    cargo_truck_1.load(7950)

    cargo_truck_1.unload(950)


    print("Individual lists------")
    data_base.list_cars()

    data_base.list_cargo_trucks()

    data_base.list_motorcycles()

    data_base.list_bicycles()









