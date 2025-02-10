
from validator import Validator
from official import Official

class Board(Official):
    def __init__(self, id, name, address, telephone_number, email_address, join_date, membership_status, role, department, board_position, position_start, position_end):
        super().__init__(id, name, address, telephone_number, email_address, join_date, membership_status, role, department)
        self.board_position = Validator.validate_name(board_position)
        self.position_start = Validator.validate_date(position_start)
        self.position_end = Validator.validate_date(position_end)

    def approve_budget(self, budget: float):
        return f"Board member {self.name} approved a budget of: ${budget}"

    def make_decision(self, decision: str):
        return f"Board member {self.name} made a decision: {decision}"




