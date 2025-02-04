import re
import os
from person import Person
from customer import Customer
from employee import Employee
from courses import Course


# Class to handle Customers, Employees, Courses
# includes load data / save data to file
# add customer / employee / course
# show customer / employee / course

# Class to handle Customers, Employees, Courses: save file / load file in txt file
class Database:
    def __init__(self):
        self.customers = self.load_data("customers.txt", Customer, 6)
        self.employees = self.load_data("employees.txt", Employee, 6)
        self.courses = self.load_data("courses.txt", Course, 4)

    def load_data(self, filename, class_, expected_fields):
        data = []
        if os.path.exists(filename):
            with open(filename, "r") as file:
                for line in file:
                    parts = line.strip().split(',')

                    # Ensure correct number of fields
                    if len(parts) == expected_fields:
                        # Create the object by passing the unpacked values from each part (input string)
                        obj = class_(*parts)
                        data.append(obj)
        return data

    def save_data(self, filename, data):
        with open(filename, "w") as file:
            for entry in data:
                # Convert object to CSV-style row without using __str__()
                if isinstance(entry, Course):
                    file.write(f"{entry.course_name},{entry.course_id},{entry.start_date},{entry.end_date}\n")
                elif isinstance(entry, Customer):
                    file.write(
                        f"{entry.full_name},{entry.address},{entry.email},{entry.telephone_number},{entry.date_of_birth},{entry.customer_id}\n")
                elif isinstance(entry, Employee):
                    file.write(
                        f"{entry.full_name},{entry.address},{entry.email},{entry.telephone_number},{entry.date_of_birth},{entry.employee_id}\n")

    def add_customer(self, customer):
        self.customers.append(customer)
        self.save_data("customers.txt", self.customers)

    def add_employee(self, employee):
        self.employees.append(employee)
        self.save_data("employees.txt", self.employees)

    def add_course(self, course):
        self.courses.append(course)
        self.save_data("courses.txt", self.courses)

    def show_all_customers(self):
        if not self.customers:
            print("No customers available.")
        else:
            print("------------- All Customers ---------------")
            for index, customer in enumerate(self.customers, start=1):
                print(f"{index}. {customer}")

    def show_all_employees(self):
        if not self.employees:
            print("No employees available.")
        else:
            print("------------- All Employees ---------------")
            for index, employee in enumerate(self.employees, start=1):
                print(f"{index}. {employee}")

    def show_all_courses(self):
        if not self.courses:
            print("No courses available.")
        else:
            print("------------- All Courses ---------------")
            for index, course in enumerate(self.courses, start=1):
                print(f"{index}. {course}")