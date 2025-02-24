

from src.models.validator import AccountValidator
from src.models.account import Account, AccountType



"""CreditAccount class - inherits from Account class"""


class CreditAccount(Account):
    def __init__(self, account_number: str, account_holder: str, balance: float, credit_limit: float):
        super().__init__(account_number, account_holder, balance, AccountType.CREDIT)
        AccountValidator.validate_positive_number(credit_limit)

        self._credit_limit = credit_limit

    # Withdraw is implemented specifically for credit accounts.
    def withdraw(self, amount):
        AccountValidator.validate_positive_number(amount)

        # Check if withdraw would exceed available credit (balance + credit limit)
        if (self._balance -amount) < - self._credit_limit:
            raise ValueError("Withdraw would exceed credit limit.")

        self._balance -= amount



    # To dict formats all the attributes of the credit account into a dictionary => serialization for json
    def to_dict(self):
        return {
            'account_number': self._account_number,
            'account_holder': self._account_holder,
            'balance': self._balance,
            'account_type': self._account_type,
            'credit_limit': self._credit_limit
        }
