from src.models.account import Account, AccountType
from src.models.validator import AccountValidator

# Debit account class
# Inherits from Account class.
class DebitAccount(Account):
    def __init__(self, account_number: str, account_holder: str, balance: float, withdrawal_limit: float):
        super().__init__(account_number, account_holder, balance, AccountType.DEBIT)
        AccountValidator.validate_positive_number(withdrawal_limit)
        self._withdrawal_limit = withdrawal_limit

    # Withdraw is implemented specifically for debit accounts.
    def withdraw(self, amount):
        AccountValidator.validate_positive_number(amount)

        if amount > 0 and amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Insufficient balance or invalid amount.")


    # To dict formats all the attributes of the debit account into a dictionary.
    def to_dict(self):
        return {
            'account_number': self._account_number,
            'account_holder': self._account_holder,
            'balance': self._balance,
            'account_type': self._account_type,
            'withdrawal_limit': self._withdrawal_limit
        }
