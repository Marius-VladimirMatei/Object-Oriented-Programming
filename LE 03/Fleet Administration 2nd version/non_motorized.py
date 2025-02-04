from vehicle import Vehicle

# class for Non Motorized vehicles


class NonMotorized(Vehicle):
    def __init__(self, id, license_plate, brand, model, year, type):
        super().__init__(id, license_plate, brand, model, year)
        self.type = type

