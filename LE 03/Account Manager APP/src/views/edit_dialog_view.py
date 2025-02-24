from typing import Optional, Dict, Any
import tkinter as tk
from tkinter import ttk, messagebox
from src.models.account import Account, AccountType


class EditDialog:
    def __init__(self, parent: tk.Tk, account: Account):
        self.dialog: tk.Toplevel
        self.account: Account = account
        self.result: Optional[Dict[str, Any]] = None
        self.holder_var: tk.StringVar
        self.limit_var: tk.StringVar

        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Edit Account")
        self.dialog.geometry("300x200")
        self.dialog.transient(parent)
        self.dialog.grab_set()

        # Center the dialog
        self.dialog.geometry("+%d+%d" % (
            parent.winfo_rootx() + parent.winfo_width() / 2 - 150,
            parent.winfo_rooty() + parent.winfo_height() / 2 - 100))

        self.create_widgets()

    def create_widgets(self) -> None:
        # Configure grid
        self.dialog.columnconfigure(1, weight=1)

        # Account Holder
        ttk.Label(self.dialog, text="Account Holder:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.holder_var = tk.StringVar(value=self.account._account_holder)
        ttk.Entry(self.dialog, textvariable=self.holder_var).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        # Limit (Credit/Withdraw)
        limit_text = "Credit Limit:" if self.account._account_type == AccountType.CREDIT else "Withdrawal Limit:"
        ttk.Label(self.dialog, text=limit_text).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        current_limit = self.account._credit_limit if self.account._account_type == AccountType.CREDIT else self.account._withdraw_limit
        self.limit_var = tk.StringVar(value=str(current_limit))
        ttk.Entry(self.dialog, textvariable=self.limit_var).grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Buttons
        btn_frame = ttk.Frame(self.dialog)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=20)

        ttk.Button(btn_frame, text="Save", command=self.save).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Cancel", command=self.cancel).pack(side=tk.LEFT, padx=5)

    def save(self) -> None:
        try:
            holder = self.holder_var.get().strip()
            limit = float(self.limit_var.get())

            if not holder:
                raise ValueError("Account holder cannot be empty")
            if limit <= 0:
                raise ValueError("Limit must be positive")

            self.result = {'holder': holder, 'limit': limit}
            self.dialog.destroy()

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def cancel(self) -> None:
        self.dialog.destroy()
