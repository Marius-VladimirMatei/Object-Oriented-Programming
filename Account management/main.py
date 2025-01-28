from account_manager import AccountManager

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
