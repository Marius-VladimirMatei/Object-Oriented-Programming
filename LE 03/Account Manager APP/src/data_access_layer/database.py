import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(
        self,
        host="localhost",
        user="root",
        password="Matei8138",
        database="account_manager",
    ):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
        self.connect()
        print("Database initialized")
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
                print("Connected to the database")

        except mysql.connector.Error as e:
            print(f"Database connection error: {e}")
            raise

    def disconnect(self):
        try:
            if hasattr(self, "connection") and self.connection.is_connected():
                if hasattr(self, "cursor"):
                    self.cursor.close()
                self.connection.close()
                print("Disconnected from the database")
        except mysql.connector.Error as e:
            print(f"Error while disconnecting: {e}")
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
            print("Tables created successfully")

        except mysql.connector.Error as e:
            # Rollback on error
            self.connection.rollback()
            print(f"Error creating tables: {e}")
            raise
        except Exception as e:
            self.connection.rollback()
            print(f"Unexpected error: {e}")
            raise

    def __del__(self):  # Finalizer function
        self.disconnect()
