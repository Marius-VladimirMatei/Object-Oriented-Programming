from src.models.account import Account, AccountType
from src.models.credit_account import CreditAccount
from src.models.debit_account import DebitAccount
from src.data_access_layer.database import Database


class DbAccountManager:
    def __init__(self):
        self.db = Database()
        self.db.connect()

    def get_accounts(self) -> dict[str, Account]:
        query = "SELECT * FROM accounts"
        self.db.cursor.execute(query)
        accounts = self.db.cursor.fetchall()

        result = {}
        for account in accounts:
            if account["account_type"] == "credit":
                a = CreditAccount(
                    account["account_number"],
                    account["account_holder"],
                    float(account["balance"]),
                    float(account["credit_limit"]),
                )
            else:
                a = DebitAccount(
                    account["account_number"],
                    account["account_holder"],
                    float(account["balance"]),
                    float(account["withdraw_limit"]),
                )

            result[a._account_number] = a

        return result

    def get_account(self, account_number: str) -> Account:
        query = "SELECT * FROM accounts WHERE account_number = %s"
        self.db.cursor.execute(query, (account_number,))
        account = self.db.cursor.fetchone()

        if account["account_type"] == "credit":
            a = CreditAccount(
                account["account_number"],
                account["account_holder"],
                float(account["balance"]),
                float(account["credit_limit"]),
            )
        else:
            a = DebitAccount(
                account["account_number"],
                account["account_holder"],
                float(account["balance"]),
                float(account["withdraw_limit"]),
            )

        return a

    def load_accounts(self):
        query = "SELECT * FROM accounts"
        self.db.cursor.execute(query)
        accounts = self.db.cursor.fetchall()

        for account in accounts:
            if account["account_type"] == "credit":
                a = CreditAccount(
                    account["account_number"],
                    account["account_holder"],
                    account["balance"],
                    account["credit_limit"],
                )
            else:
                a = DebitAccount(
                    account["account_number"],
                    account["account_holder"],
                    account["balance"],
                    account["withdraw_limit"],
                )

            self.add_account(a)

    def update_account(self, account: Account):
        if account._account_type == AccountType.CREDIT:
            self._update_credit_account(account)
        else:
            self._update_debit_account(account)

    def _update_credit_account(self, account: CreditAccount):
        query = "UPDATE accounts SET account_holder = %s, balance = %s, credit_limit = %s WHERE account_number = %s"
        self.db.cursor.execute(
            query,
            (
                account._account_holder,
                account._balance,
                account._credit_limit,
                account._account_number,
            ),
        )
        self.db.connection.commit()

    def _update_debit_account(self, account: DebitAccount):
        query = "UPDATE accounts SET account_holder = %s, balance = %s, withdraw_limit = %s WHERE account_number = %s"
        self.db.cursor.execute(
            query,
            (
                account._account_holder,
                account._balance,
                account._withdraw_limit,
                account._account_number,
            ),
        )
        self.db.connection.commit()

    def add_account(self, account: Account):
        if account._account_type == AccountType.CREDIT:
            self._add_credit_account(account)
        else:
            self._add_debit_account(account)

    def _add_credit_account(self, account: CreditAccount):
        query = "INSERT INTO accounts (account_number, account_holder, balance, credit_limit, account_type) VALUES (%s, %s, %s, %s, 'credit')"
        self.db.cursor.execute(
            query,
            (
                account._account_number,
                account._account_holder,
                account._balance,
                account._credit_limit,
            ),
        )
        self.db.connection.commit()

    def _add_debit_account(self, account: DebitAccount):
        query = "INSERT INTO accounts (account_number, account_holder, balance, withdraw_limit, account_type) VALUES (%s, %s, %s, %s, 'debit')"
        self.db.cursor.execute(
            query,
            (
                account._account_number,
                account._account_holder,
                account._balance,
                account._withdraw_limit,
            ),
        )
        self.db.connection.commit()

    def delete_account(self, account_number: str):
        query = "DELETE FROM accounts WHERE account_number = %s"
        self.db.cursor.execute(query, (account_number,))
        self.db.connection.commit()
