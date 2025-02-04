# Account manager app

class Account:
    # Represents a single account

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


class AccountManager:
    # Manages multiple accounts

# No need for other parameters than self because initializes an empty dictionary {} to store and manage multiple accounts
# Does not need any initial data from the user
# Accounts are later created with create_account method

    def __init__(self):
        self.accounts = {}

# Create new account
    def create_account(self, account_number, account_holder, balance=0.0):
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")

        if not isinstance(account_holder, str):
            raise ValueError("Account holder must be a string.")

        if not isinstance(balance, (int, float)):
            raise ValueError("Balance must be a positive number.")

        if account_number in self.accounts:
            print(f"Account number {account_number} already exists.")
        else:
            new_account = Account(account_number, account_holder, balance)
            self.accounts[account_number] =  new_account
            print(f"Account {account_number} for {account_holder} created successfully.")

# Delete an existing account
    def delete_account(self, account_number):
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")

        if account_number in self.accounts:
            del self.accounts[account_number]   # del statement removes the specific account number. del self.accounts=> deletes the entire dictionary
            print(f"Account {account_number} deleted successfully.")

        else:
            print(f"Account {account_number} does not exist.")

# Withdraw money from a specific account
    def withdraw_money(self, account_number, amount):

        if not isinstance(account_number, int):
            raise ValueError("Account number must be a number.")

        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a positive number.")

        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)

        else:
            print(f"Account {account_number} does not exist.")

# Deposit money into a specific account
    def deposit_money(self, account_number, amount):

        if not isinstance(account_number, int):
            raise ValueError("Account number must be an number.")

        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a positive.")

        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)

        else:
            print(f"Account {account_number} does not exist.")


# Calculate total balance across all accounts
    # this function could be used when the same person has multiple accounts and wants to see the total sum balance.
    def calculate_total_balance(self):

        total_balance = sum(account.balance for account in self.accounts.values())
        # .values method accesses and displays the values from the dictionary {key: "value, "}
        print(f"Total balance across all accounts: {total_balance}")
        return total_balance

# Function to return balance for specific account
    def account_balance(self, account_number):
        if not isinstance(account_number, int):
            raise ValueError("Enter an existing account number.")

    # Check for account existence
        if account_number in self.accounts:
            account = self.accounts[account_number]
            print(f"Account {account_number} balance is: {account.balance}")
        else:
            raise ValueError(f"Account number {account_number} does not exist.")



# Display details for a specific account
    def display_individual_account(self, account_number):

        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")

        if account_number in self.accounts:
            self.accounts[account_number].display_account_info()
        else:
            print(f"Account {account_number} does not exist.")

# Display data from all accounts
    def display_all_accounts(self):

        if self.accounts:
            for account in self.accounts.values():
                account.display_account_info()
                print("-----------------------")
        else:
            print("No accounts to display.")


# Usage
if __name__ == "__main__":
    manager = AccountManager()

# Create accounts
    print("\n Creating accounts:")
    manager.create_account(101, "Alice", 500)
    manager.create_account(102, "Bob", 1000)


# Deposit money using the new deposit_money function
    print("\n Deposit:")
    manager.deposit_money(101, 300)  # Deposit 300 into Alice account
    manager.deposit_money(102, 500)  # Deposit 500 into Bob's account


# Withdraw money
    print("\n Withdraw:")
    manager.withdraw_money(101, 200)  # Withdraw 200 from Alice account
    manager.withdraw_money(102, 400)  # Withdraw 400 from Bob account

    print()

# Display individual account
    print("\n Individual Account Data:")
    manager.display_individual_account(101)  # Display Alice account


# Display all accounts
    print("\n All Accounts Data:")
    manager.display_all_accounts()


# Calculate total balance
    print("\n Calculating Total Balance:")
    manager.calculate_total_balance()

# Account balance for specific
    manager.account_balance(101)
    manager.account_balance(102)

    # Delete an account
    print("\n Deleting an Account:")
    manager.delete_account(101)


# Display all accounts after deletion
    print("\n All Accounts Data After Deletion:")
    manager.display_all_accounts()

