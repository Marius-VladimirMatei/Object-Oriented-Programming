import re
from club import Club
from member import Member
from official import Official, Board


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