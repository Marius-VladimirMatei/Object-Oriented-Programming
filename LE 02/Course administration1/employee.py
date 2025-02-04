import re
from person import Person

class Employee(Person):
    def __init__(self, name, address, post_code, telephone, email, employee_id, position):
        # Call the parent class's constructor
        super().__init__(name, address, post_code, telephone, email)

        # Validate the employee_id and position
        if not isinstance(employee_id, int) or not re.match(r"^\d{3}$", str(employee_id)):
            raise ValueError("Employee ID must contain 3 digits.")

        if not isinstance(position, str) or not re.match(r"^[äÄöÖüÜßA-Za-z\s]+$", str(position)):
            raise TypeError("Please insert valid entry for position")

        self.employee_id = employee_id
        self.position = position

    # Return a string representation that includes class's details
    def __str__(self):
        return f"{super().__str__()}, Employee ID: {self.employee_id}, Position: {self.position}"