import json
from validator import Validator


class Member:
    def __init__(self, id, name, address, telephone_number, email_address, join_date, membership_status):
        # Validate and set attributes
        self.id = int(Validator.validate_numeric(str(id)))
        self.name = Validator.validate_name(name)
        self.address = Validator.validate_address(address)
        self.telephone_number = Validator.validate_telephone(telephone_number)
        self.email_address = Validator.validate_email(email_address)
        self.join_date = Validator.validate_date(join_date)  # Expected format: DD/MM/YYYY
        self.membership_status = membership_status


    def to_dict(self):
        """Convert the Member instance into a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "telephone_number": self.telephone_number,
            "email_address": self.email_address,
            "join_date": self.join_date,
            "membership_status": self.membership_status
        }

    def update_member_details(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                if key == "id":
                    validated_value = int(Validator.validate_numeric(str(value)))
                elif key == "name":
                    validated_value = Validator.validate_name(value)
                elif key == "address":
                    validated_value = Validator.validate_address(value)
                elif key == "telephone_number":
                    validated_value = Validator.validate_telephone(value)
                elif key == "email_address":
                    validated_value = Validator.validate_email(value)
                elif key == "join_date":
                    validated_value = Validator.validate_date(value)
                elif key == "membership_status":
                    validated_value = value  # Boolean; no regex validation needed
                else:
                    validated_value = value
                setattr(self, key, validated_value)
                print(f"Updated {key} to {validated_value} for member {self.name}")
            else:
                print(f"{key} is not a valid attribute for Member.")
        print(f"Member details updated for: {self.name}")


    def pay_dues(self, amount: float):
        print(f"Member {self.name} paid dues: {amount}")


# Define the external file for saving members
file_name = "members_data.json"


 # Save the list of member dictionaries back to the JSON file
def save_members(members):
    with open(file_name, "w") as f:
        json.dump(members, f, indent=4)



 # Add a new member to the JSON file
def add_member(member):
    members = load_members()
    members.append(member.to_dict())
    save_members(members)



 # Remove a member by their id from the JSON file.
def remove_member(member_id):

    members = load_members()
    # Filter  the member with the matching id
    new_members = [m for m in members if m.get("id") != member_id]

    if len(new_members) == len(members):
        print(f"No member found with id: {member_id}")
    else:
        save_members(new_members)



# Load members from the JSON file.
def load_members():

    try:
        with open(file_name, "r") as f:
            members = json.load(f)

            if not isinstance(members, list):
                members = [members]
            return members
    except (FileNotFoundError, json.JSONDecodeError):
        return []


""" Update the member record in the JSON file with the details of updated_member.
    The function finds the member by their id, updates the record, and saves the file. """

def update_member_in_file(updated_member: Member):

    members = load_members()
    for index, member_data in enumerate(members):
        if member_data.get("id") == updated_member.id:
            members[index] = updated_member.to_dict()
            break
    else:
        print(f"No member found with id: {updated_member.id}")
        return
    save_members(members)
    print(f"Member with id {updated_member.id} has been updated in the file.")


def show_all_members():

    """Loads all members from the JSON file, formats their details into a string,
    and returns that string to be later used in a GUI interface """

    members = load_members()
    if not members:
        return "No members found."

    output = "=== All Members ===\n\n"
    for member in members:
        output += f"ID: {member.get('id')}\n"
        output += f"Name: {member.get('name')}\n"
        output += f"Address: {member.get('address')}\n"
        output += f"Telephone Number: {member.get('telephone_number')}\n"
        output += f"Email Address: {member.get('email_address')}\n"
        output += f"Join Date: {member.get('join_date')}\n"
        output += f"Membership Status: {member.get('membership_status')}\n"
        output += "-" * 40 + "\n"
    return output

