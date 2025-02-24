from typing import Any
import tkinter as tk
from tkinter import ttk, messagebox

from src.models.account import AccountType
from src.views.create_account_view import CreateAccountView
from src.views.edit_dialog_view import EditDialog
from datetime import datetime
from src.controllers.account_controller import AccountController


class AccountView:
    def __init__(self, root: tk.Tk, controller: AccountController):
        self.root: tk.Tk = root
        self.controller: AccountController = controller
        self.tree: ttk.Treeview
        self.search_var: tk.StringVar
        self.amount_var: tk.StringVar
        self.accounts_tab: ttk.Frame
        self.create_tab: ttk.Frame
        self.create_account_form: CreateAccountView
        self.create_widgets()

    def create_widgets(self) -> None:
        # Configure root window to be responsive
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=0)  # Status bar row

        # Create notebook for tabs
        notebook = ttk.Notebook(self.root)
        notebook.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        # Create tabs
        self.accounts_tab = ttk.Frame(notebook)
        self.create_tab = ttk.Frame(notebook)

        # Configure tab grid weights
        self.accounts_tab.columnconfigure(0, weight=1)
        self.accounts_tab.rowconfigure(1, weight=1)  # Make the treeview expand
        self.create_tab.columnconfigure(0, weight=1)

        notebook.add(self.accounts_tab, text="View Accounts")
        notebook.add(self.create_tab, text="Create Account")

        # Initialize views
        self.create_accounts_list()
        self.create_account_form = CreateAccountView(
            self.create_tab, self.controller, self.refresh_accounts
        )

    def create_accounts_list(self) -> None:
        # Add search frame
        search_frame = ttk.Frame(self.accounts_tab)
        search_frame.grid(row=0, column=0, pady=(10, 0), padx=10, sticky="ew")
        search_frame.columnconfigure(1, weight=1)  # Make search entry expand

        ttk.Label(search_frame, text="Search:").grid(row=0, column=0, padx=5)
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *args: self.filter_accounts())
        ttk.Entry(search_frame, textvariable=self.search_var).grid(
            row=0, column=1, padx=5, sticky="ew"
        )

        # Create and configure the treeview
        columns = ("Account Number", "Holder", "Type", "Balance", "Limit")
        self.tree = ttk.Treeview(self.accounts_tab, columns=columns, show="headings")

        # Set column headings and widths
        for col in columns:
            self.tree.heading(col, text=col)
            if col in ["Account Number", "Holder"]:
                self.tree.column(col, width=150, minwidth=100)
            elif col in ["Type"]:
                self.tree.column(col, width=100, minwidth=80)
            else:  # Balance and Limit columns
                self.tree.column(col, width=100, minwidth=80, anchor="e")

        # Add scrollbars
        y_scrollbar = ttk.Scrollbar(
            self.accounts_tab, orient="vertical", command=self.tree.yview
        )
        x_scrollbar = ttk.Scrollbar(
            self.accounts_tab, orient="horizontal", command=self.tree.xview
        )
        self.tree.configure(
            yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set
        )

        # Grid layout
        self.tree.grid(row=1, column=0, sticky="nsew", padx=10)
        y_scrollbar.grid(row=1, column=1, sticky="ns")
        x_scrollbar.grid(row=2, column=0, sticky="ew")

        # Transaction Frame
        trans_frame = ttk.LabelFrame(self.accounts_tab, text="Transactions")
        trans_frame.grid(row=3, column=0, pady=10, padx=10, sticky="ew")
        trans_frame.columnconfigure(1, weight=1)

        ttk.Label(trans_frame, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
        self.amount_var = tk.StringVar()
        ttk.Entry(trans_frame, textvariable=self.amount_var).grid(
            row=0, column=1, padx=5, pady=5, sticky="ew"
        )

        # Buttons frame
        btn_frame = ttk.Frame(trans_frame)
        btn_frame.grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(btn_frame, text="Deposit", command=self.deposit).pack(
            side=tk.LEFT, padx=2
        )
        ttk.Button(btn_frame, text="Withdraw", command=self.withdraw).pack(
            side=tk.LEFT, padx=2
        )

        # Account management buttons
        mgmt_frame = ttk.Frame(trans_frame)
        mgmt_frame.grid(row=0, column=3, padx=5, pady=5)
        ttk.Button(mgmt_frame, text="Edit", command=self.edit_account).pack(
            side=tk.LEFT, padx=2
        )
        ttk.Button(mgmt_frame, text="Delete", command=self.delete_account).pack(
            side=tk.LEFT, padx=2
        )

        self.refresh_accounts()

    def refresh_accounts(self) -> None:
        # Clear the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Repopulate with current accounts
        accounts = self.controller.get_accounts()
        for account in accounts.values():
            limit = (
                account._credit_limit
                if account._account_type == AccountType.CREDIT
                else account._withdraw_limit
            )
            self.tree.insert(
                "",
                tk.END,
                values=(
                    account._account_number,
                    account._account_holder,
                    str(account._account_type.value),
                    f"€{account._balance:,.2f}",
                    f"€{limit:,.2f}",
                ),
            )

    def edit_account(self) -> None:
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select an account to edit")
            return

        account_number = self.tree.item(selected[0])["values"][0]
        account = self.controller.get_accounts()[account_number]

        dialog = EditDialog(self.root, account)
        self.root.wait_window(dialog.dialog)

        if dialog.result:
            try:
                self.controller.update_account(
                    account_number, dialog.result["holder"], dialog.result["limit"]
                )
                self.refresh_accounts()
                messagebox.showinfo("Success", "Account updated successfully!")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def delete_account(self) -> None:
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning(
                "No Selection", "Please select an account to delete."
            )
            return

        if messagebox.askyesno(
            "Confirm Delete", "Are you sure you want to delete this account?"
        ):
            account_number = self.tree.item(selected[0])["values"][0]
            self.controller.delete_account(account_number)
            self.refresh_accounts()

    def deposit(self) -> None:
        self.perform_transaction("deposit")

    def withdraw(self) -> None:
        self.perform_transaction("withdraw")

    def perform_transaction(self, transaction_type: str) -> None:
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select an account")
            return

        try:
            amount = float(self.amount_var.get())
            account_number = self.tree.item(selected[0])["values"][0]

            self.controller.perform_transaction(
                account_number, amount, transaction_type
            )

            # Update UI
            self.refresh_accounts()
            self.amount_var.set("")  # Clear amount field

            messagebox.showinfo(
                "Success", f"{transaction_type.capitalize()} successful!"
            )

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def filter_accounts(self, *args: Any) -> None:
        search_term = self.search_var.get().lower()

        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Add filtered accounts to treeview
        accounts = self.controller.get_accounts()
        for account in accounts.values():
            if (
                search_term in account._account_number.lower()
                or search_term in str(account._account_type.value).lower()
                or search_term in account._account_holder.lower()
            ):
                limit = (
                    account._credit_limit
                    if hasattr(account, "_credit_limit")
                    else account._withdraw_limit
                )
                self.tree.insert(
                    "",
                    "end",
                    values=(
                        account._account_number,
                        account._account_holder,
                        str(account._account_type.value),
                        f"€{account._balance:.2f}",
                        f"€{limit:.2f}",
                    ),
                )
