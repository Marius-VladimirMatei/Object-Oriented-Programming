from account import Account

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