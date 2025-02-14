import tkinter as tk
from tkinter import ttk, messagebox
from member import Member
from official import Official
from board import Board

class UpdateMemberTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Row for entering the member ID to load
        tk.Label(self, text="Member ID to update:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.id_entry = tk.Entry(self, width=20)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self, text="Load", command=self.load_member).grid(row=0, column=2, padx=5, pady=5)

        # Labels for common and optional fields (always visible)
        labels = [
            ("Name", "name"),
            ("Address", "address"),
            ("Telephone", "telephone_number"),
            ("Email", "email_address"),
            ("Join Date (DD/MM/YYYY)", "join_date"),
            ("Membership Status", "membership_status"),
            ("Role", "role"),
            ("Department", "department"),
            ("Board Position", "board_position"),
            ("Position Start (DD/MM/YYYY)", "position_start"),
            ("Position End (DD/MM/YYYY)", "position_end")
        ]

        self.entries = {}
        row = 1
        for label_text, key in labels:
            tk.Label(self, text=label_text + ":").grid(row=row, column=0, padx=5, pady=3, sticky="w")
            entry = tk.Entry(self, width=30)
            entry.grid(row=row, column=1, padx=5, pady=3)
            self.entries[key] = entry
            row += 1

        tk.Button(self, text="Update Member", command=self.update_member)\
            .grid(row=row, column=0, columnspan=2, pady=10)

    def load_member(self):
        member_id_str = self.id_entry.get().strip()
        if not member_id_str.isdigit():
            messagebox.showerror("Error", "Please enter a valid numeric ID.")
            return
        member_id = int(member_id_str)
        members = Member.load_members()
        member_data = next((m for m in members if m.get("id") == member_id), None)
        if not member_data:
            messagebox.showerror("Error", f"No member found with ID {member_id}")
            return

        # Fill the fields from the JSON record
        for key, entry in self.entries.items():
            entry.config(state="normal")
            entry.delete(0, tk.END)
            entry.insert(0, str(member_data.get(key, "")))

        # Prevent editing of the ID field
        self.id_entry.config(state="disabled")

    def update_member(self):
        # Gather data from the fields
        data = { key: entry.get().strip() for key, entry in self.entries.items() }
        member_id = self.id_entry.get().strip()

        # Determine member type based on the optional fields:
        # - If "board_position" is filled, treat as Board, elif "role" is filled, treat as Official, else regular Member.
        try:
            if data.get("board_position"):
                updated_member = Board(
                    member_id,
                    data.get("name"),
                    data.get("address"),
                    data.get("telephone_number"),
                    data.get("email_address"),
                    data.get("join_date"),
                    data.get("membership_status"),
                    data.get("role"),
                    data.get("department"),
                    data.get("board_position"),
                    data.get("position_start"),
                    data.get("position_end")
                )
            elif data.get("role"):
                updated_member = Official(
                    member_id,
                    data.get("name"),
                    data.get("address"),
                    data.get("telephone_number"),
                    data.get("email_address"),
                    data.get("join_date"),
                    data.get("membership_status"),
                    data.get("role"),
                    data.get("department")
                )
            else:
                updated_member = Member(
                    member_id,
                    data.get("name"),
                    data.get("address"),
                    data.get("telephone_number"),
                    data.get("email_address"),
                    data.get("join_date"),
                    data.get("membership_status")
                )
            Member.update_member_in_file(updated_member)
            messagebox.showinfo("Success", "Member updated successfully!")
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_fields(self):
        # Clear all fields and allow editing of the ID again.
        for entry in self.entries.values():
            entry.config(state="normal")
            entry.delete(0, tk.END)
        self.id_entry.config(state="normal")
        self.id_entry.delete(0, tk.END)
