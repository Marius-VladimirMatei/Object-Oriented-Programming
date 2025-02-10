
import re

class Validator:
    @staticmethod
    def validate_name(name):
        """
        Validates that a name contains only letters (including umlauts and ß), spaces, apostrophes, and hyphens.
        """
        pattern = r"^[A-Za-zäöüÄÖÜß\s'-]+$"
        if re.match(pattern, name):
            return name.strip()
        else:
            raise ValueError(f"Invalid name format: {name}")

    @staticmethod
    def validate_address(address):
        """
        Validates that an address contains only letters (with umlauts and ß), numbers, spaces, apostrophes, and hyphens.
        """
        pattern = r"^[A-Za-zäöüÄÖÜß0-9\s'-]+$"
        if re.match(pattern, address):
            return address.strip()
        else:
            raise ValueError(f"Invalid address format: {address}")

    @staticmethod
    def validate_email(email):
        """
        Validates an email address.
        """
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, email):
            return email.strip()
        else:
            raise ValueError(f"Invalid email format: {email}")

    @staticmethod
    def validate_telephone(telephone):
        """
        Validates a telephone number that may contain digits, spaces, plus signs, apostrophes, or hyphens.
        """
        pattern = r"^[0-9\s'+-]+$"
        if re.match(pattern, telephone):
            return telephone.strip()
        else:
            raise ValueError(f"Invalid telephone format: {telephone}")

    @staticmethod
    def validate_date(date_str):
        """
        Validates that the date string is in the DD/MM/YYYY format.
        """
        pattern = r"^\d{2}/\d{2}/\d{4}$"
        if re.match(pattern, date_str):
            return date_str
        else:
            raise ValueError(f"Invalid date format (expected DD/MM/YYYY): {date_str}")

    @staticmethod
    def validate_numeric(value):
        """
        Validates that the value contains only numeric digits.
        """
        pattern = r"^\d+$"
        if re.match(pattern, value):
            return value
        else:
            raise ValueError(f"Invalid numeric value: {value}")
