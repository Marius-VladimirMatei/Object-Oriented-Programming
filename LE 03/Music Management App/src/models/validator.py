import re


class Validator:
    @staticmethod
    def validate_name(name):
        """
        Validates that a name contains only letters (including umlauts and ß), spaces, apostrophes, and hyphens.
        """
        pattern = r"^[/A-Za-zäöüÄÖÜß\s'-]+$"
        if re.match(pattern, name):
            return name.strip()
        else:
            raise ValueError(f"Invalid name format: {name}")

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
    def validate_string(value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string.")
        if len(value) == 0:
            raise ValueError("Value must not be empty.")
        else:
            return value

    @staticmethod
    def validate_number(value):
        if not isinstance(value, (int)):
            raise ValueError("Value must be a number.")
        else:
            return value

    @staticmethod
    def validate_track_list(value: list[str]):
        if not isinstance(value, list):
            raise ValueError("Value must be a list.")

        validated_list = []
        for item in value:
            validated_list.append(Validator.validate_string(item))

        return validated_list
