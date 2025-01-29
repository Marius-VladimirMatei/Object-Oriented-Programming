import re
from person import Person
from customer import Customer
from employee import Employee
from courses import Course
from database import Database

# General function for validating user input
def get_input(prompt, pattern, error_message):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Error: This field cannot be empty. Please enter a valid value.")
            continue
        if re.match(pattern, value):
            return value
        else:
            print(error_message)

# Add new customer cu data base
def add_new_customer(db):
    full_name = get_input("Enter full name: ", r"^[A-Za-zäöüÄÖÜß\s'-]+$", "Invalid name format.")
    address = get_input("Enter full address: ", r"^[A-Za-zäöüÄÖÜß0-9\s'-]+$", "Invalid address format.")
    email = get_input("Enter email: ", r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", "Invalid email format.")
    telephone_number = get_input("Enter telephone: ", r"^[0-9\s'+-`]+$", "Invalid telephone format.")
    date_of_birth = get_input("Enter date of birth: ", r"^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$","The date of birth must be in the format DD/MM/YYYY.")
    customer_id = get_input("Enter Customer ID: ", r"^\d+$", "Customer ID must be numeric.")

    new_customer = Customer(full_name, address, email, telephone_number, date_of_birth, customer_id)
    db.add_customer(new_customer)
    print("Customer added successfully!")


# Add new employee cu data base
def add_new_employee(db):
    full_name = get_input("Enter full name: ", r"^[A-Za-zäöüÄÖÜß\s'-]+$", "Invalid name format.")
    address = get_input("Enter full address: ", r"^[A-Za-zäöüÄÖÜß0-9\s'-]+$", "Invalid address format.")
    email = get_input("Enter email: ", r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", "Invalid email format.")
    telephone_number = get_input("Enter telephone: ", r"^[0-9\s'+-`]+$", "Invalid telephone format.")
    date_of_birth = get_input("Enter date of birth: ", r"^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$", "The date of birth must be in the format DD/MM/YYYY.")
    employee_id = get_input("Enter Employee ID: ", r"^\d+$", "Employee ID must be numeric.")

    new_employee = Employee(full_name, address, email, telephone_number, date_of_birth, employee_id)
    db.add_employee(new_employee)
    print("Employee added successfully!")


# Add new course cu data base
def add_new_course(db):
    course_name = input("Enter Course Name: ")
    course_id = get_input("Enter Course ID: ", r"^\d+$", "Course ID must be numeric.")
    start_date = get_input("Enter start date: ", r"^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$", "The date must be in the format DD/MM/YYYY.")
    end_date = get_input("Enter end date: ", r"^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$", "The date must be in the format DD/MM/YYYY.")

    new_course = Course(course_name, course_id, start_date, end_date)
    db.add_course(new_course)
    print("Course added successfully!")




# Function to edit a customer or employee
def edit_person(db, is_customer=True):
    if is_customer:
        people = db.customers
        filename = "customers.txt"
        print("Editing Customer")
    else:
        people = db.employees
        filename = "employees.txt"
        print("Editing Employee")

    if not people:
        print("No records available to edit.")
        return

    # Show list of customers/employees
    for index, person in enumerate(people, start=1):
        print(f"{index}. {person}")

    try:
        choice = int(input("Enter the number of the person to edit: ")) - 1
        if choice < 0 or choice >= len(people):
            print("Invalid selection.")
            return

        person = people[choice]

        # Allow updating fields
        person.full_name = input(f"Enter new full name ({person.full_name}): ") or person.full_name
        person.address = input(f"Enter new address ({person.address}): ") or person.address
        person.email = input(f"Enter new email ({person.email}): ") or person.email
        person.telephone_number = input(f"Enter new telephone number ({person.telephone_number}): ") or person.telephone_number
        person.date_of_birth = input(f"Enter new date of birth ({person.date_of_birth}): ") or person.date_of_birth

        if is_customer:
            person.customer_id = input(f"Enter new Customer ID ({person.customer_id}): ") or person.customer_id
        else:
            person.employee_id = input(f"Enter new Employee ID ({person.employee_id}): ") or person.employee_id

        db.save_data(filename, people)
        print("Record updated successfully!")

    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    db = Database()

    while True:
        print("\nMenu:")
        print("1. Add Customer")
        print("2. Add Employee")
        print("3. Add Course")
        print("4. Edit Customer")
        print("5. Edit Employee")
        print("6. Show Customers")
        print("7. Show Employees")
        print("8. Show Courses")
        print("9. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            add_new_customer(db)
        elif choice == "2":
            add_new_employee(db)
        elif choice == "3":
            add_new_course(db)
        elif choice == "4":
            edit_person(db, is_customer=True)
        elif choice == "5":
            edit_person(db, is_customer=False)
        elif choice == "6":
            db.show_all_customers()
        elif choice == "7":
            db.show_all_employees()
        elif choice == "8":
            db.show_all_courses()
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
