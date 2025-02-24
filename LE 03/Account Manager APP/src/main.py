import tkinter as tk

from src.views.account_view import AccountView

from src.controllers.account_controller import AccountController
from src.models.db_account_manager import DbAccountManager


def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Account Management System")

    # Initialize MVC components
    account_manager = DbAccountManager()

    controller = AccountController(account_manager)
    app = AccountView(root, controller)

    root.mainloop()


if __name__ == "__main__":
    main()
