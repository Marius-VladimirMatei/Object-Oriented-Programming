# class for courses

class Course:
    def __init__(self, course_name, course_id, start_date, end_date):
        self.course_name = course_name
        self.course_id = course_id
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"Course Name: {self.course_name}, Course ID: {self.course_id}, Start Date: {self.start_date}, End Date: {self.end_date}"
