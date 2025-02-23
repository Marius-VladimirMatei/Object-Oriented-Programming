
class AccountValidator:
    @staticmethod
    def validate_number(value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a number.")

    @staticmethod
    def validate_positive_number(value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a number.")
        if value <= 0:
            raise ValueError("Value must be positive.")

    @staticmethod
    def validate_string(value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string.")
        if len(value) == 0:
            raise ValueError("Value must not be empty.")
