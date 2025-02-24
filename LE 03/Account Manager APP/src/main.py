import tkinter as tk

from src.views.account_view import AccountView

from src.controllers.account_controller import AccountController
from src.models.account_manager import AccountManager



def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Account Management System")

    # Initialize MVC components
    account_manager = AccountManager()
    try:
        account_manager = AccountManager.load_accounts("accounts.json")
    except:
        pass

    controller = AccountController(account_manager)
    app = AccountView(root, controller)

    root.mainloop()


if __name__ == "__main__":
    main()
