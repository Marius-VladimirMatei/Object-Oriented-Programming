from abc import ABC, abstractmethod
from enum import Enum
from validator import AccountValidator

class AccountType(str, Enum):
    CREDIT = 'credit'
    DEBIT = 'debit'

class Account(ABC):
    def __init__(self, account_number: str, account_holder: str, balance: float, account_type: AccountType):
        AccountValidator.validate_number(account_number)
        AccountValidator.validate_string(account_holder)
        AccountValidator.validate_number(balance)

        # _ making all attributes "protected" => convention used to mark all the attributes within the class or its subclasses
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = balance
        self._account_type = account_type


    def deposit(self, amount):
        """"Deposit method is common to all accounts"""
        AccountValidator.validate_positive_number(amount)
        self._balance +=amount

    def get_balance(self):
        """"Deposit method is common to all accounts"""
        return self._balance

    @abstractmethod
    def withdraw(self, amount):
        """ Withdraw method is different for each type of account, hence is different. """
        pass


    @abstractmethod
    def to_dict(self):
        """ To dict method is different for each type of account, hence it is abstract.
               (each account type has different attributes) """
        pass
