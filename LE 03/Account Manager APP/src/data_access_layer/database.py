import mysql.connector
from mysql.connector import Error
import os


class Database:
    def __init__(self):
        # get the database credentials from the environment variables instead of hardcoding them
        host = os.getenv("DATABASE_HOST")
        user = os.getenv("DATABASE_USER")
        password = os.getenv("DATABASE_PASSWORD")
        database = os.getenv("DATABASE_DB")

        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
        self.connect()
        self.create_tables()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=3306,
                user=self.user,
                password=self.password,
                database=self.database,
                autocommit=False,  # Disable autocommit for transaction control
            )

            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                # Create database if doesn't exist
                self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
                self.cursor.execute(f"USE {self.database}")

        except mysql.connector.Error as e:
            raise

    def disconnect(self):
        try:
            if hasattr(self, "connection") and self.connection.is_connected():
                if hasattr(self, "cursor"):
                    self.cursor.close()
                self.connection.close()
        except mysql.connector.Error as e:
            raise

    def create_tables(self):
        try:
            # Start transaction
            self.connection.start_transaction()

            create_accounts_table = """
            CREATE TABLE IF NOT EXISTS accounts (
                account_number VARCHAR(50) PRIMARY KEY,
                account_holder VARCHAR(100) NOT NULL,
                balance DECIMAL(10, 2) NOT NULL,
                account_type ENUM('credit', 'debit') NOT NULL,
                credit_limit DECIMAL(10, 2),
                withdraw_limit DECIMAL(10, 2)
            )
            """
            self.cursor.execute(create_accounts_table)

            # Commit transaction
            self.connection.commit()

        except mysql.connector.Error as e:
            # Rollback on error
            self.connection.rollback()
            raise
        except Exception as e:
            self.connection.rollback()
            raise

    def __del__(self):  # Finalizer function
        self.disconnect()
