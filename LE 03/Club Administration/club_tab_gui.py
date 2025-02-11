
import tkinter as tk
from tkinter import ttk, messagebox
from club import Club

class ClubTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Club Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.club_name_entry = tk.Entry(self, width=30)
        self.club_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text="Address:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.club_address_entry = tk.Entry(self, width=30)
        self.club_address_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self, text="Telephone:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.club_tel_entry = tk.Entry(self, width=30)
        self.club_tel_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self, text="Email:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.club_email_entry = tk.Entry(self, width=30)
        self.club_email_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Button(self, text="Create Club", command=self.create_club)\
            .grid(row=4, column=0, columnspan=2, pady=10)

        tk.Button(self, text="Show Last Club Details", command=self.show_club_details)\
            .grid(row=5, column=0, columnspan=2, pady=10)

    def create_club(self):
        name = self.club_name_entry.get()
        address = self.club_address_entry.get()
        telephone = self.club_tel_entry.get()
        email = self.club_email_entry.get()
        try:
            club = Club.create_club(name, address, telephone, email)
            messagebox.showinfo("Success", f"Club created:\n{club.get_club_details()}")
            self.club_name_entry.delete(0, tk.END)
            self.club_address_entry.delete(0, tk.END)
            self.club_tel_entry.delete(0, tk.END)
            self.club_email_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_club_details(self):
        if Club.clubs:
            last_club = Club.clubs[-1]
            details = last_club.get_club_details()
            messagebox.showinfo("Club Details", details)
        else:
            messagebox.showinfo("Club Details", "No clubs created yet.")
