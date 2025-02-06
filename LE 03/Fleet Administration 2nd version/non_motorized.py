from vehicle import Vehicle

# class for Non Motorized vehicles


class NonMotorized(Vehicle):
    def __init__(self, id, brand, model, year, type):
        super().__init__(id, brand, model, year)
        self.type = type

