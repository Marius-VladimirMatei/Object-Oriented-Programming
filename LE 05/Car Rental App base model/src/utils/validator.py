import re
from datetime import datetime  # Add this import at the top


class Validator:
    @staticmethod
    def validate_name(name):
        """
        Validates that a name contains only letters (including umlauts and ß), spaces, apostrophes, and hyphens.
        """
        if not isinstance(name, str):
            raise ValueError("Name must be a string")

        if len(name.strip()) == 0:
            raise ValueError("Name cannot be empty")

        pattern = r"^[A-Za-zäöüÄÖÜß\s'-]+$"
        if re.match(pattern, name):
            return name.strip()
        else:
            raise ValueError(f"Invalid name format: {name}")

    @staticmethod
    def validate_string(value):
        """Basic string validation - checks if non-empty string"""
        if not isinstance(value, str):
            raise ValueError("Value must be a string")

        if len(value.strip()) == 0:
            raise ValueError("Value cannot be empty")

        return value.strip()

    @staticmethod
    def validate_number(value):
        """General validation for numeric values"""
        if isinstance(value, (int, float)):
            return value

        try:
            # Try to convert string to number
            return int(value)
        except (ValueError, TypeError):
            raise ValueError(f"Value must be a number: {value}")

    @staticmethod
    def validate_id(value):
        """General validation for numeric values"""
        if isinstance(value, (int)):
            return value

        try:
            # Try to convert string to number
            return int(value)
        except (ValueError, TypeError):
            raise ValueError(f"Value must be a number: {value}")

    @staticmethod
    def validate_year(value):
        """Specifically validates a year value"""
        try:
            year = int(value)
        except (ValueError, TypeError):
            raise ValueError(f"Year must be a number: {value}")

        # Check reasonable range for a car year
        if year < 1900 or year > 2100:
            raise ValueError(f"Year {year} is out of reasonable range (1900-2100)")

        return year

    @staticmethod
    def validate_telephone(telephone):
        """
        Validates a telephone number that may contain digits, spaces, plus signs, and hyphens.
        """
        if not isinstance(telephone, str):
            raise ValueError("Telephone must be a string")

        # Allow digits, spaces, plus signs, and hyphens
        pattern = r"^[0-9\s+\-()]+$"
        if re.match(pattern, telephone) and len(telephone.strip()) > 0:
            return telephone.strip()
        else:
            raise ValueError(f"Invalid telephone format: {telephone}")

    @staticmethod
    def validate_email(email):
        """
        Validates that the string is a properly formatted email address.
        """
        if not isinstance(email, str):
            raise ValueError("Email must be a string")

        if len(email.strip()) == 0:
            raise ValueError("Email cannot be empty")

        # Basic email validation pattern
        pattern = r"^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, email):
            return email.strip()
        else:
            raise ValueError(f"Invalid email format: {email}")

    @staticmethod
    def validate_address(address):
        """
        Validates that an address contains only allowed characters.
        """
        if not isinstance(address, str):
            raise ValueError("Address must be a string")

        if len(address.strip()) == 0:
            raise ValueError("Address cannot be empty")

        # Allow letters, numbers, spaces, commas, periods, hyphens, slashes, and hashtags
        pattern = r"^[A-Za-z0-9äöüÄÖÜß\s,.'\-/#]+$"
        if re.match(pattern, address):
            return address.strip()
        else:
            raise ValueError(f"Invalid address format: {address}")

    @staticmethod
    def validate_date(date_str, format="%d-%m-%Y"):
        """
        Validates that the date string is in the specified format.
        Default format is DD-MM-YYYY for rentals.
        """
        try:
            # Check if date can be parsed in the specified format
            date_obj = datetime.strptime(date_str, format)
            return date_str
        except ValueError:
            expected_format = "DD-MM-YYYY" if format == "%d-%m-%Y" else format
            raise ValueError(
                f"Invalid date format (expected {expected_format}): {date_str}"
            )

    @staticmethod
    def validate_rental_dates(start_date, end_date):
        """
        Validates that rental start and end dates are valid:
        1. Both are valid dates
        2. End date is not before start date
        """
        # Validate basic date format
        start = Validator.validate_date(start_date)
        end = Validator.validate_date(end_date)

        # Check date order
        start_obj = datetime.strptime(start, "%d-%m-%Y")
        end_obj = datetime.strptime(end, "%d-%m-%Y")

        if end_obj < start_obj:
            raise ValueError("End date cannot be before start date")

        return start, end
