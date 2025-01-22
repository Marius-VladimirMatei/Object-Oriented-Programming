import re

class Club:
    def __init__(self, name, address, telephone, email):
        self.name = self.validate_name(name)
        self.address = self.validate_address(address)
        self.telephone = self.validate_phone(telephone)
        self.email = self.validate_email(email)
        self.members = []  # List to hold the members

    def add_member(self, member):
        self.members.append(member)
        print(f"Added member: {member.name}")  # Print the name of the member

    def remove_member(self, id):
        self.members = [m for m in self.members if m.id != id]
        print(f"Member removed")

    def get_club_details(self):
        return f"Club DETAILS: Name: {self.name}, Address: {self.address}, Phone: {self.telephone}, Email: {self.email}"

    @staticmethod
    def validate_name(name):
        if re.match(r"^[A-Za-z\s]+$", name):
            return name
        else:
            raise ValueError(f"Invalid name: {name}")

    @staticmethod
    def validate_address(address):
        if re.match(r"^[ÖöÜüßÄäA-Za-z0-9\s,.-]+$", address):
            return address
        else:
            raise ValueError(f"Invalid address: {address}")

    @staticmethod
    def validate_phone(telephone):
        pattern = r"^\+?\d{1,4}?[-.\s]?\(?\d+\)?[-.\s]?\d{1,5}[-.\s]?\d{1,5}[-.\s]?\d{1,5}$"
        if re.match(pattern, telephone):
            return telephone
        else:
            raise ValueError(f"Invalid phone number: {telephone}")

    @staticmethod
    def validate_email(email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(pattern, email):
            return email
        else:
            raise ValueError(f"Invalid email address: {email}")


# Inherits from Club
class Member:
    def __init__(self, id, name, address, telephone, email, join_date, membership_status):
        self.id = id
        self.name = self.validate_name(name)
        self.address = self.validate_address(address)
        self.telephone = self.validate_phone(telephone)
        self.email = self.validate_email(email)
        self.join_date = self.validate_date(join_date)
        self.membership_status = self.validate_membership_status(membership_status)

    @staticmethod
    def validate_name(name):
        if re.match(r"^[A-Za-z\s]+$", name):
            return name
        else:
            raise ValueError(f"Invalid name: {name}")

    @staticmethod
    def validate_address(address):
        if re.match(r"^[A-Za-z0-9\s,.-]+$", address):
            return address
        else:
            raise ValueError(f"Invalid address: {address}")

    @staticmethod
    def validate_phone(telephone):
        pattern = r"^\+?\d{1,4}?[-.\s]?\(?\d+\)?[-.\s]?\d{1,5}[-.\s]?\d{1,5}[-.\s]?\d{1,5}$"
        if re.match(pattern, telephone):
            return telephone
        else:
            raise ValueError(f"Invalid phone number: {telephone}")

    @staticmethod
    def validate_email(email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(pattern, email):
            return email
        else:
            raise ValueError(f"Invalid email address: {email}")

    @staticmethod
    def validate_date(join_date):
        pattern = r"^\d{4}-\d{2}-\d{2}$"  # Format: YYYY-MM-DD
        if re.match(pattern, join_date):
            return join_date
        else:
            raise ValueError(f"Invalid date format: {join_date}")

    @staticmethod
    def validate_membership_status(membership_status):
        if membership_status in ["Active", "Inactive"]:
            return membership_status
        else:
            raise ValueError(f"Invalid membership status: {membership_status}")

    def pay_dues(self):
        print(f"Member: {self.name} has paid dues")

    def update_member_details(self, name=None, membership_status=None):
        if name:
            self.name = name
        if membership_status:
            self.membership_status = membership_status
        print(f"Updated details for {self.name}: Status - {self.membership_status}")

    def get_member_info(self):
        return f"Member INFO: ID: {self.id}, Name: {self.name}, Status: {self.membership_status}"


class Official(Member):
    def __init__(self, id, name, address, telephone, email, join_date, membership_status, role, department):
        super().__init__(id, name, address, telephone, email, join_date, membership_status)  # Initialize parent (Member)
        self.role = role
        self.department = department

    def assign_role(self, role):
        self.role = role
        print(f"{self.name} assigned role: {self.role}")

    def schedule_meeting(self, date):
        print(f"Meeting scheduled on {date} by {self.name}.")


class Board(Official):
    def __init__(self, id, name, address, telephone, email, join_date, membership_status, role, department, board_position, position_start, position_end):
        super().__init__(id, name, address, telephone, email, join_date, membership_status, role, department)
        self.board_position = board_position
        self.position_start = position_start
        self.position_end = position_end

    def approve_budget(self, amount):
        print(f"Budget of {amount} approved by {self.name}, Position: {self.board_position}")

    def make_decision(self, decision):
        print(f"Decision made by {self.name}: {decision}")


# Create Club
print()
print("Create club")
club_1 = Club("Chess Club", "Graz 106, Österreich", "06763216549", "contact@chessclub.com")
print(club_1.get_club_details())

print()
print("Create members")
# Create members
member_1 = Member(
    "M001",
    "Alice",
    "Eckertstrasse 20",
    "06761234567",
    "alice@example.com",
    "2025-01-15",
    "Active"
)

member_2 = Member(
    "M002",
    "Bob",
    "Wienerstrass 288",
    "0676654987657",
    "bob@example.com",
    "2024-11-20",
    "Inactive"
)
club_1.add_member(member_1)
club_1.add_member(member_2)

# Show member info
print(member_1.get_member_info())

# Remove member
club_1.remove_member("M001")

print()
print("Update member details")
# Update member details
member_2.update_member_details(name="Bobobobo", membership_status="Active")
print(member_2.get_member_info())

print()
print("Create official member")
# Create Official
official_1 = Official(
    "001",
    "Charles",
    "Wien 123",
    "06761234567",
    "charles@chessclub.com",
    "2023-02-01",
    "Active",
    "Event Manager",
    "Events"
)
club_1.add_member(official_1)

# Assign a new role to the official
print("Assign role")
official_1.assign_role("Chief Coordinator")

# Schedule a meeting
print("Schedule meeting")
official_1.schedule_meeting("2025-02-10")

print()
print("Create board member")
# Create Board Member
board_member_1 = Board(
    "B002",
    "John",
    "Graz",
    "06761234567",
    "john@mail.com",
    "2020-08-15",
    "Active",
    "Chairperson",  # role for Official
    "Board",         # department for Official
    "Board Member",  # board_position
    "2023-01-01",    # position_start
    "2025-12-31"     # position_end
)
club_1.add_member(board_member_1)

print()
# Approve budget
print("Budget approve")
board_member_1.approve_budget(50000)

print()
# Make decision
print("Decision make")
board_member_1.make_decision("Approve new training programs for members.")
