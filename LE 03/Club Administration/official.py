
from validator import Validator
from member import Member

class Official(Member):
    def __init__(self, id, name, address, telephone_number, email_address, join_date, membership_status, role, department):
        super().__init__(id, name, address, telephone_number, email_address, join_date, membership_status)
        self.role = Validator.validate_name(role)
        self.department = Validator.validate_name(department)

    def assign_role(self, role: str):
        self.role = Validator.validate_name(role)
        return f"Assigned role '{self.role}' to official {self.name}"

    def schedule_meeting(self, meeting_time: str):
        return f"Official {self.name} has scheduled a meeting at {meeting_time}"
