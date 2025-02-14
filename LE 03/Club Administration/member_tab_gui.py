
import tkinter as tk
from tkinter import ttk, messagebox
from member import Member
from official import Official
from board import Board

class MemberTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Select Member Type:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.member_type_var = tk.StringVar(value="Member")
        member_type_menu = tk.OptionMenu(self, self.member_type_var, "Member", "Official", "Board", command=self.update_member_fields)
        member_type_menu.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text="ID:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.id_entry = tk.Entry(self, width=30)
        self.id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self, text="Name:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.name_entry = tk.Entry(self, width=30)
        self.name_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self, text="Address:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.address_entry = tk.Entry(self, width=30)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self, text="Telephone:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.telephone_entry = tk.Entry(self, width=30)
        self.telephone_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self, text="Email:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.email_entry = tk.Entry(self, width=30)
        self.email_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(self, text="Join Date (DD/MM/YYYY):").grid(row=6, column=0, sticky="w", padx=5, pady=5)
        self.join_date_entry = tk.Entry(self, width=30)
        self.join_date_entry.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(self, text="Membership Status (True/False):").grid(row=7, column=0, sticky="w", padx=5, pady=5)
        self.membership_status_entry = tk.Entry(self, width=30)
        self.membership_status_entry.grid(row=7, column=1, padx=5, pady=5)

        # Extra fields for Official and Board
        self.role_label = tk.Label(self, text="Role:")
        self.role_entry = tk.Entry(self, width=30)
        self.department_label = tk.Label(self, text="Department:")
        self.department_entry = tk.Entry(self, width=30)
        self.board_position_label = tk.Label(self, text="Board Position:")
        self.board_position_entry = tk.Entry(self, width=30)
        self.position_start_label = tk.Label(self, text="Position Start (DD/MM/YYYY):")
        self.position_start_entry = tk.Entry(self, width=30)
        self.position_end_label = tk.Label(self, text="Position End (DD/MM/YYYY):")
        self.position_end_entry = tk.Entry(self, width=30)

        self.update_member_fields(self.member_type_var.get())

        tk.Button(self, text="Submit Member", command=self.submit_member)\
            .grid(row=13, column=0, columnspan=2, pady=10)

    def update_member_fields(self, *args):
        # Hide all extra fields first
        self.role_label.grid_forget()
        self.role_entry.grid_forget()
        self.department_label.grid_forget()
        self.department_entry.grid_forget()
        self.board_position_label.grid_forget()
        self.board_position_entry.grid_forget()
        self.position_start_label.grid_forget()
        self.position_start_entry.grid_forget()
        self.position_end_label.grid_forget()
        self.position_end_entry.grid_forget()

        member_type = self.member_type_var.get()
        if member_type == "Official":
            self.role_label.grid(row=8, column=0, sticky="w", padx=5, pady=5)
            self.role_entry.grid(row=8, column=1, padx=5, pady=5)
            self.department_label.grid(row=9, column=0, sticky="w", padx=5, pady=5)
            self.department_entry.grid(row=9, column=1, padx=5, pady=5)
        elif member_type == "Board":
            self.role_label.grid(row=8, column=0, sticky="w", padx=5, pady=5)
            self.role_entry.grid(row=8, column=1, padx=5, pady=5)
            self.department_label.grid(row=9, column=0, sticky="w", padx=5, pady=5)
            self.department_entry.grid(row=9, column=1, padx=5, pady=5)
            self.board_position_label.grid(row=10, column=0, sticky="w", padx=5, pady=5)
            self.board_position_entry.grid(row=10, column=1, padx=5, pady=5)
            self.position_start_label.grid(row=11, column=0, sticky="w", padx=5, pady=5)
            self.position_start_entry.grid(row=11, column=1, padx=5, pady=5)
            self.position_end_label.grid(row=12, column=0, sticky="w", padx=5, pady=5)
            self.position_end_entry.grid(row=12, column=1, padx=5, pady=5)

    def submit_member(self):
        member_type = self.member_type_var.get()
        id_val = self.id_entry.get()
        name_val = self.name_entry.get()
        address_val = self.address_entry.get()
        telephone_val = self.telephone_entry.get()
        email_val = self.email_entry.get()
        join_date_val = self.join_date_entry.get()
        membership_status_val = self.membership_status_entry.get()

        try:
            if member_type == "Member":
                new_member = Member(
                    id_val, name_val, address_val, telephone_val,
                    email_val, join_date_val, membership_status_val
                )
            elif member_type == "Official":
                role_val = self.role_entry.get()
                department_val = self.department_entry.get()
                new_member = Official(
                    id_val, name_val, address_val, telephone_val,
                    email_val, join_date_val, membership_status_val,
                    role_val, department_val
                )
            elif member_type == "Board":
                role_val = self.role_entry.get()
                department_val = self.department_entry.get()
                board_position_val = self.board_position_entry.get()
                position_start_val = self.position_start_entry.get()
                position_end_val = self.position_end_entry.get()
                new_member = Board(
                    id_val, name_val, address_val, telephone_val,
                    email_val, join_date_val, membership_status_val,
                    role_val, department_val, board_position_val,
                    position_start_val, position_end_val
                )
            else:
                raise ValueError("Unknown member type selected.")

            Member.add_member(new_member)  # Use the class method on Member
            messagebox.showinfo("Success", f"{member_type} created successfully!")
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_fields(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.telephone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.join_date_entry.delete(0, tk.END)
        self.membership_status_entry.delete(0, tk.END)
        self.role_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)
        self.board_position_entry.delete(0, tk.END)
        self.position_start_entry.delete(0, tk.END)
        self.position_end_entry.delete(0, tk.END)



