from person import Person
from customer import Customer
from employee import Employee
from file_manager import FileManager



# main.py (or any script to test the FileManager)



if __name__ == "__main__":
    # Create some sample objects
    c1 = Customer("Max Mustermann", "Main Street 123", "1234", "+1 555 1234", "max@example.com", 100)
    c2 = Customer("Erika Mustermann", "Broadway 10", "2345", "+1 555 5678", "erika@example.com", 101)
    e1 = Employee("Anna Schmidt", "2nd Avenue", "3456", "+1 555 9999", "anna@example.com", 200, "Manager")

    # Prepare a list to save
    data_to_save = [c1, c2, e1]

    # Filename to store data
    filename = "people_data.txt"

    # Append objects to file
    FileManager.append_to_file(filename, data_to_save)
    print(f"Appended {len(data_to_save)} records to '{filename}'.")

    # Read objects back from file
    loaded_objects = FileManager.read_from_file(filename)
    print(f"\nLoaded {len(loaded_objects)} objects from '{filename}':")
    for obj in loaded_objects:
        print(obj)  # Uses each class's __str__ method





try:
    person = Person("John Doe",
                    "123 Elm Street",
                    "8020",
                    "+1-234-567-890",
                    "john.doe@example.com")
    print(person.name, person.address, person.telephone, person.email)
except (TypeError, ValueError) as e:
    print(e)


try:
    employee_1 = Employee("James Brown",
                          "Main Street 987 New York",
                          "8010",
                          "06761234567",
                          "james@brown.com",
                          100,
                          "Cashier")
    print(employee_1.name, employee_1.employee_id)
except (TypeError, ValueError) as e:
    print(e)





