
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


    # Override the base to_dict method to include the additional fields specific to an Official
    def to_dict(self):

        data = super().to_dict()  # Base dictionary data from Member.to_dict()

        # Add Official-specific attributes
        data['role'] = self.role
        data['department'] = self.department
        return data