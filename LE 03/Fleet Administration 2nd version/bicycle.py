from non_motorized import NonMotorized

# class for Bicycle objects

class Bicycle(NonMotorized):
    def __init__(self, id, brand, model, year, type, gear_count):
        super().__init__(id, brand, model, year, type)
        self.gear_count = gear_count