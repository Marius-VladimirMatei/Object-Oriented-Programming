
import tkinter as tk
from tkinter import ttk
from club_tab_gui import ClubTab
from member_tab_gui import MemberTab
from show_members_tab_gui import ShowMembersTab
from update_member_tab_gui import UpdateMemberTab


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Club and Member Management")
        self.geometry("600x500")  # Optional: set the window size

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        # Create tabs
        self.club_tab = ClubTab(self.notebook)
        self.member_tab = MemberTab(self.notebook)
        self.show_members_tab = ShowMembersTab(self.notebook)
        self.update_member_tab = UpdateMemberTab(self.notebook)

        # Add tabs to notebook
        self.notebook.add(self.club_tab, text="Create Club")
        self.notebook.add(self.member_tab, text="Create Member")
        self.notebook.add(self.show_members_tab, text="Show Members")
        self.notebook.add(self.update_member_tab, text="Update Member")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()