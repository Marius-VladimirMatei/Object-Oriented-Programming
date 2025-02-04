from person import Person

# class for Employee

class Employee(Person):
    def __init__(self, full_name, address, email, telephone_number, date_of_birth, employee_id):
        super().__init__(full_name, address, email, telephone_number, date_of_birth)
        self.employee_id = employee_id

    def __str__(self):
        return f"{super().__str__()}, Employee ID: {self.employee_id}"
