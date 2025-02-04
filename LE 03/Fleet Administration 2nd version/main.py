from vehicle import Vehicle
from motoritzed import Motorized
from non_motorized import NonMotorized
from car import Car
from cargo_truck import Cargo_truck
from motorcycle import Motorcycle
from bicycle import Bicycle


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


car_1.refuel(55)

cargo_truck_1.load(7950)

cargo_truck_1.unload(950)