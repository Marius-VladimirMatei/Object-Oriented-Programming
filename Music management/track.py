class Track:
    def __init__(self, title, file_name, length):
        self.title = title
        self.file_name = file_name
        self.length = length  # Format: "HH:MM:SS"


    def get_length_in_seconds(self):
        hours, minutes, seconds = map(int, self.length.split(":"))  # map converts each string into an integer
        return hours * 3600 + minutes * 60 + seconds

    def __str__(self):
        return f"{self.title}, duration: [{self.length}]"
