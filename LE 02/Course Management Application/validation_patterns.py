import re

# all validation patterns

def validate_name(name):
    pattern = r"^[A-Za-zäöüÄÖÜß\s'-]+$"
    return re.match(pattern, name) is not None

def validate_address(address):
    pattern = r"^[A-Za-zäöüÄÖÜß0-9\s'-]+$"
    return re.match(pattern, address) is not None

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def validate_telephone(telephone):
    pattern = r"^[0-9\s'+-]+$"
    return re.match(pattern, telephone) is not None

def validate_date(date):
    pattern = r"^\d{2}/\d{2}/\d{4}$"
    return re.match(pattern, date) is not None

def validate_numeric(value):
    pattern = r"^\d+$"
    return re.match(pattern, value) is not None

def get_valid_input(prompt, validation_function, error_message):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Error: This field cannot be empty. Please enter a valid value.")
            continue
        if validation_function(value):
            return value
        else:
            print(error_message)
