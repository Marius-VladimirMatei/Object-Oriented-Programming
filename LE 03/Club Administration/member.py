import json
import os
from validator import Validator

class Member:
    file_name = "members_data.json"  # Define the external file for saving members

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
        # Convert the Member instance into a dictionary for JSON serialization
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

    # Save the list of member dictionaries back to the JSON file
    @classmethod
    def save_member(cls, member):
        with open(cls.file_name, "a", encoding="utf-8") as f:
            # Write compact JSON (no indent) so that each member is on a single line
            json.dump(member.to_dict(), f, separators=(',', ':'))
            f.write("\n")
        print(f"Member {member.name} saved (appended) to file.")

    @classmethod
    def load_members(cls):
        members = []
        try:
            with open(cls.file_name, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        members.append(json.loads(line))
            return members
        except FileNotFoundError:
            return []

    # Add a new member to the JSON file by appending it to the file
    @classmethod
    def add_member(cls, member):
        cls.save_member(member)

    # Remove a member by their id from the JSON file.
    @classmethod
    def remove_member(cls, member_id):
        members = cls.load_members()
        new_members = [m for m in members if m.get("id") != member_id]
        if len(new_members) == len(members):
            print(f"No member found with id: {member_id}")
        else:
            with open(cls.file_name, "w", encoding="utf-8") as f:
                for mem in new_members:
                    f.write(json.dumps(mem, separators=(',', ':')) + "\n")
            print(f"Member with id {member_id} has been removed.")


    # Update the member record in the JSON file with the details of updated_member.
    # The function finds the member by their id, updates the record, and saves the file.
    @classmethod
    def update_member_in_file(cls, updated_member):
        members = cls.load_members()
        updated = False
        for index, member_data in enumerate(members):
            if member_data.get("id") == updated_member.id:
                members[index] = updated_member.to_dict()
                updated = True
                break
        if not updated:
            print(f"No member found with id: {updated_member.id}")
            return
        with open(cls.file_name, "w", encoding="utf-8") as f:
            for mem in members:
                f.write(json.dumps(mem, separators=(',', ':')) + "\n")
        print(f"Member with id {updated_member.id} has been updated in the file.")



    @classmethod
    def show_all_members(cls):
        members = cls.load_members()
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

            # Check for optional fields (if any)
            if member.get('role') is not None:
                output += f"Role: {member.get('role')}\n"
            if member.get('department') is not None:
                output += f"Department: {member.get('department')}\n"
            if member.get('board_position') is not None:
                output += f"Board Position: {member.get('board_position')}\n"
            if member.get('position_start') is not None:
                output += f"Position Start: {member.get('position_start')}\n"
            if member.get('position_end') is not None:
                output += f"Position End: {member.get('position_end')}\n"

            output += "--------\n"
        return output
