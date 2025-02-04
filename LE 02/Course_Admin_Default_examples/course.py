import re

class Course():
    def __init__(self, course_name, start_date, end_date):

        # Input validations
        if not isinstance(course_name, str):
            raise TypeError("Enter a valid course name.")

        date_pattern = r"^\d{4}-\d{2}-\d{2}$"
        if not re.match(date_pattern, start_date) or not re.match(date_pattern, end_date):
            raise ValueError("Enter a valid start date in the format YYYY-MM-DD.")

        self.course_name = course_name
        self.start_date = start_date
        self.end_date = end_date


    def __str__(self):
        return f"Course name: {self.course_name}, Starts: {self.start_date}, Ends: {self.end_date}"

