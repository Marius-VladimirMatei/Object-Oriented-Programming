class Account:
    # Represents a single account
    # Class and methods

    def __init__(self, account_number, account_holder, balance=0.0):

        if not isinstance(account_number, int):
            raise ValueError("Account number must be a positive number.")

        if not isinstance(account_holder, str):
            raise ValueError("Account holder must be text.")

        if not isinstance(balance, (int, float)):
            raise ValueError("Balance must be a positive number.")

        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

# Deposit money into the account
    def deposit(self, amount):

        if not isinstance(amount, (int, float)):
            raise ValueError("Deposit amount must be a positive number.")

        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited into account {self.account_number}. New balance: {self.balance}")

        else:
            print("Deposit amount must be positive.")

# Withdraw money from the account
    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Withdrawal amount must be a number.")

        #if 0 < amount <= self.balance:

        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn from account {self.account_number}. New balance: {self.balance}")

        else:
            print("Insufficient balance or invalid amount.")

# Display account details
    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")