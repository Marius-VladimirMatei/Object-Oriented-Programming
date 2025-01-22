

class Club:
    def __init__(self, name, address, telephone_number, email_address):
        self.name = name
        self.address = address
        self.telephone_number = telephone_number
        self.email_address = email_address
        # list to hold the members
        self.member = []

    def add_member(self, member):
        self.members.append(member)
        print(f"Added member: {member.name}")

    def remove_member(self, id):
        self.member = [m for m in self.member if m.id != id]
        print(f"Member removed.")

    def get_details(self):
        return f"Club: {self.name}, Address: {self.address}, Telephone: {self.telephone_number}, Email: {self.email_address}"


# Inherits from Club
class Member(Club):
    def __init__(self, id, name, address, telephone_number, email_address, join_date, membership_status):
        super().__init__(name, address, telephone_number, email_address)
        self.id = id
        self.join_date = join_date
        self.membership_status = membership_status

    def pay_dues(self):
        print(f"Member {self.name} has paid dues.")

    def update_details(self, name=None, membership_status=None):
        if name:
            self.name = name
        if membership_status:
            self.membership_status = membership_status

    def get_info(self):
        return f"ID: {self.id}, Name: {self.name}, Status: {self.membership_status}"



class Official(Member):
    def __init__(self, id, name, address, telephone_number, email_address, join_date, membership_status, role, department):
        super().__init__(name, address, telephone_number, email_address, id, join_date, membership_status)
        self.role = role
        self.department = department

    def assign_role(self, role):
        self.role = role
        print(f"{self.name} assigned role: {self.role}")

    def schedule_meeting(self, date):
        print(f"Meeting scheduled on {date} by {self.name}.")



class Board(Official):
    def __init__(self, id, name, address, telephone_number, email_address, join_date, membership_status, department, board_position, position_start, position_end):
        super().__init__(self, id, name, address, telephone_number, email_address, join_date, membership_status, department)
        self.board_position = board_position
        self.position_start = position_start
        self.position_end = position_end

    def approve_budget(self, amount):
        print(f"Budget of {amount} approved by {self.name}, Position: {self.board_position}")

    def make_decision(self, decision):
        print(f"Decision made by {self.name}: {decision}")


# Create a club
club = Club("Chess Club", "Augasse 106", "06763216549", "contact@chessclub.com")

# Create members
member1 = Member("M001", "Alice", "Eckertstrasse 20", "06761234567", "alice@example.com", "2025-01-15", "Active")
member2 = Member("M002", "Bob", "Wienerstrass 288", "0676654987657", "bob@example.com", "2024-11-20", "Inactive")

# Add members to the club
print(club.add_member(member1))
club.add_member(member2)

# Display club details
print(f"Club Name: {club.name}")
for m in club.members:
    print(m.get_info())

print(club.get_details())

print(m.remove_member(member1))

# Create a club and add a member
club = Club("Book Club", "123 Oak St", "555-3456", "info@bookclub.com")
member = Member("M003", "Ella", "999 Willow Ln", "555-1111", "ella@example.com", "2024-05-15", "Active")
club.add_member(member)

# Update member details
member.update_details(name="Ella Smith", membership_status="Inactive")
print(member.get_info())

# Remove the member from the club
club.remove_member("M003")
print(f"Remaining members in club: {[m.name for m in club.members]}")



# Create a board member

board_member_2 = Board("B002", "John", "Graz", "06761234567", "john@mail.com", "2020-08-15","Active", "Board", "Chairperson", "2023-01-01", "2025-12-31")

# Approve a budget
board_member_2.approve_budget(50000)

# Make a decision
board_member_2.make_decision("Approve new training programs for members.")
