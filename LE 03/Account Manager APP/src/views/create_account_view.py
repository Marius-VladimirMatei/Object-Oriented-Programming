from typing import Any, Callable
import tkinter as tk
from tkinter import ttk, messagebox
from src.controllers.account_controller import AccountController


class CreateAccountView:
    def __init__(self, parent: ttk.Frame, controller: AccountController, refresh_callback: Callable[[], None]):
        self.parent: ttk.Frame = parent
        self.controller: AccountController = controller
        self.refresh_callback: Callable[[], None] = refresh_callback
        self.account_type: tk.StringVar
        self.account_number: tk.StringVar
        self.account_holder: tk.StringVar
        self.initial_balance: tk.StringVar
        self.limit: tk.StringVar
        self.limit_label: ttk.Label
        self.create_widgets()

    def create_widgets(self) -> None:
        # Account Creation Form
        form_frame = ttk.LabelFrame(self.parent, text="New Account")
        form_frame.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        # Configure form grid
        form_frame.columnconfigure(1, weight=1)

        # Account Type
        ttk.Label(form_frame, text="Account Type:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        type_frame = ttk.Frame(form_frame)
        type_frame.grid(row=0, column=1, sticky="ew")

        self.account_type = tk.StringVar(value="debit")
        ttk.Radiobutton(type_frame, text="Debit", variable=self.account_type,
                        value="debit").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(type_frame, text="Credit", variable=self.account_type,
                        value="credit").pack(side=tk.LEFT, padx=5)

        # Account Number
        ttk.Label(form_frame, text="Account Number:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.account_number = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.account_number).grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Account Holder
        ttk.Label(form_frame, text="Account Holder:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.account_holder = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.account_holder).grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # Initial Balance
        ttk.Label(form_frame, text="Initial Balance:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.initial_balance = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.initial_balance).grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        # Credit/Withdraw Limit
        self.limit_label = ttk.Label(form_frame, text="Withdraw Limit:")
        self.limit_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.limit = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.limit).grid(row=4, column=1, padx=5, pady=5, sticky="ew")

        # Update limit label when account type changes
        self.account_type.trace_add("write", self.update_limit_label)

        # Submit Button
        submit_frame = ttk.Frame(form_frame)
        submit_frame.grid(row=5, column=0, columnspan=2, pady=15)
        ttk.Button(submit_frame, text="Create Account", command=self.create_account).pack()

    def update_limit_label(self, *args: Any) -> None:
        limit_type = "Credit Limit:" if self.account_type.get() == "credit" else "Withdraw Limit:"
        self.limit_label.config(text=limit_type)

    def create_account(self) -> None:
        try:
            # Get values from form
            account_type = self.account_type.get()
            account_number = self.account_number.get().strip()
            holder = self.account_holder.get().strip()

            # Validate and convert numeric inputs
            try:
                balance = float(self.initial_balance.get())
                limit = float(self.limit.get())
            except ValueError:
                raise ValueError("Balance and limit must be valid numbers")

            if not account_number or not holder:
                raise ValueError("All fields are required")

            # Create the account
            self.controller.create_account(
                account_type,
                account_number,
                holder,
                balance,
                limit
            )

            # Clear form
            self.account_number.set("")
            self.account_holder.set("")
            self.initial_balance.set("")
            self.limit.set("")

            # Show success message
            messagebox.showinfo("Success", "Account created successfully!")

            # Refresh the accounts list
            self.refresh_callback()

        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create account: {str(e)}")
