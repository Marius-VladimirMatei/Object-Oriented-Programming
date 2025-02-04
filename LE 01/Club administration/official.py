import re
from member import Member

# Official and Board classes

class Official(Member):
    def __init__(self, id, name, address, telephone, email, join_date, membership_status, role, department):
        if not all(isinstance(arg, str) for arg in
                   [id, name, address, telephone, email, join_date, membership_status, role, department]):
            raise TypeError("All input arguments must be strings.")

        super().__init__(id, name, address, telephone, email, join_date, membership_status)  # Initialize parent (Member)

        self.role = role
        self.department = department

    def assign_role(self, role):
        self.role = role
        print(f"{self.name} assigned role: {self.role}")

    def schedule_meeting(self, date):
        print(f"Meeting scheduled on {date} by {self.name}.")


class Board(Member):
    def __init__(self, id, name, address, telephone, email, join_date, membership_status, role, department, board_position, position_start, position_end):
        if not all(isinstance(arg, str) for arg in
                   [id, name, address, telephone, email, join_date, membership_status, role, department, board_position, position_start, position_end]):
            raise TypeError("All input arguments must be strings.")

        super().__init__(id, name, address, telephone, email, join_date, membership_status)

        self.role = role
        self.department = department
        self.board_position = board_position
        self.position_start = position_start
        self.position_end = position_end

    def approve_budget(self, amount):
        print(f"Budget of {amount} approved by {self.name}, Position: {self.board_position}")

    def make_decision(self, decision):
        print(f"Decision made by {self.name}: {decision}")