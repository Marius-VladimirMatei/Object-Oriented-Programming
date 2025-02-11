
import tkinter as tk
from tkinter import ttk, messagebox
from member import show_all_members

class ShowMembersTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.text_area = tk.Text(self, wrap="word", width=80, height=20)
        self.text_area.pack(expand=True, fill="both", padx=5, pady=5)
        tk.Button(self, text="Show all entries", command=self.refresh_members)\
            .pack(pady=5)

    def refresh_members(self):
        try:
            members_text = show_all_members()
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, members_text)
        except Exception as e:
            messagebox.showerror("Error", str(e))
