class SystemMetric:
    # Class representing a system metric with a name and value.

    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value

    def __str__(self):
        # String representation for end users

        return f"{self.name}: {self.value}"
