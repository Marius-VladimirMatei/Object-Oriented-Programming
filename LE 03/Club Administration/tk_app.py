import tkinter as tk
from tkinter import ttk, messagebox

from club import Club
from member import Member, add_member, show_all_members
from official import Official
from board import Board

# Create the main window
root = tk.Tk()
root.title("Club and Member Management")

# Create a Notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=10, pady=10)

# ----- Club Creation Tab -----
club_frame = ttk.Frame(notebook)
notebook.add(club_frame, text="Create Club")

tk.Label(club_frame, text="Club Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
club_name_entry = tk.Entry(club_frame, width=30)
club_name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(club_frame, text="Address:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
club_address_entry = tk.Entry(club_frame, width=30)
club_address_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(club_frame, text="Telephone:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
club_tel_entry = tk.Entry(club_frame, width=30)
club_tel_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(club_frame, text="Email:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
club_email_entry = tk.Entry(club_frame, width=30)
club_email_entry.grid(row=3, column=1, padx=5, pady=5)

#
tk.Button(
    club_frame,
    text="Create Club",
    command=lambda: messagebox.showinfo("Info", "Create Club functionality")
).grid(row=4, column=0, columnspan=2, pady=10)

# ----- Member Creation Tab -----
member_frame = ttk.Frame(notebook)
notebook.add(member_frame, text="Create Member")

tk.Label(member_frame, text="Select Member Type:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
member_type_var = tk.StringVar(value="Member")
member_type_menu = tk.OptionMenu(member_frame, member_type_var, "Member", "Official", "Board")
member_type_menu.grid(row=0, column=1, padx=5, pady=5)

tk.Label(member_frame, text="ID:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
id_entry = tk.Entry(member_frame, width=30)
id_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(member_frame, text="Name:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
name_entry = tk.Entry(member_frame, width=30)
name_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(member_frame, text="Address:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
address_entry = tk.Entry(member_frame, width=30)
address_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(member_frame, text="Telephone:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
telephone_entry = tk.Entry(member_frame, width=30)
telephone_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(member_frame, text="Email:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
email_entry = tk.Entry(member_frame, width=30)
email_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(member_frame, text="Join Date (DD/MM/YYYY):").grid(row=6, column=0, sticky="w", padx=5, pady=5)
join_date_entry = tk.Entry(member_frame, width=30)
join_date_entry.grid(row=6, column=1, padx=5, pady=5)

tk.Label(member_frame, text="Membership Status (True/False):").grid(row=7, column=0, sticky="w", padx=5, pady=5)
membership_status_entry = tk.Entry(member_frame, width=30)
membership_status_entry.grid(row=7, column=1, padx=5, pady=5)

# Extra fields for Official and Board types
role_label = tk.Label(member_frame, text="Role:")
role_entry = tk.Entry(member_frame, width=30)
department_label = tk.Label(member_frame, text="Department:")
department_entry = tk.Entry(member_frame, width=30)
board_position_label = tk.Label(member_frame, text="Board Position:")
board_position_entry = tk.Entry(member_frame, width=30)
position_start_label = tk.Label(member_frame, text="Position Start (DD/MM/YYYY):")
position_start_entry = tk.Entry(member_frame, width=30)
position_end_label = tk.Label(member_frame, text="Position End (DD/MM/YYYY):")
position_end_entry = tk.Entry(member_frame, width=30)


def update_member_fields(*args):
    # Hide extra fields
    role_label.grid_forget()
    role_entry.grid_forget()
    department_label.grid_forget()
    department_entry.grid_forget()
    board_position_label.grid_forget()
    board_position_entry.grid_forget()
    position_start_label.grid_forget()
    position_start_entry.grid_forget()
    position_end_label.grid_forget()
    position_end_entry.grid_forget()

    member_type = member_type_var.get()
    if member_type == "Official":
        role_label.grid(row=8, column=0, sticky="w", padx=5, pady=5)
        role_entry.grid(row=8, column=1, padx=5, pady=5)
        department_label.grid(row=9, column=0, sticky="w", padx=5, pady=5)
        department_entry.grid(row=9, column=1, padx=5, pady=5)
    elif member_type == "Board":
        role_label.grid(row=8, column=0, sticky="w", padx=5, pady=5)
        role_entry.grid(row=8, column=1, padx=5, pady=5)
        department_label.grid(row=9, column=0, sticky="w", padx=5, pady=5)
        department_entry.grid(row=9, column=1, padx=5, pady=5)
        board_position_label.grid(row=10, column=0, sticky="w", padx=5, pady=5)
        board_position_entry.grid(row=10, column=1, padx=5, pady=5)
        position_start_label.grid(row=11, column=0, sticky="w", padx=5, pady=5)
        position_start_entry.grid(row=11, column=1, padx=5, pady=5)
        position_end_label.grid(row=12, column=0, sticky="w", padx=5, pady=5)
        position_end_entry.grid(row=12, column=1, padx=5, pady=5)


member_type_var.trace("w", update_member_fields)
update_member_fields()

# ----- Show Members Tab -----
show_members_frame = ttk.Frame(notebook)
notebook.add(show_members_frame, text="Show Members")

text_area = tk.Text(show_members_frame, wrap="word", width=80, height=20)
text_area.pack(expand=True, fill="both", padx=5, pady=5)

#
tk.Button(
    show_members_frame,
    text="Refresh List",
    command=lambda: messagebox.showinfo("Info", "Refresh List")
).pack(pady=5)

# Start the GUI event loop
root.mainloop()
