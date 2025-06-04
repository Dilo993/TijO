class LastNameValidator:
    def __init__(self, last_name):
        self.last_name = last_name

    def is_valid(self):
        return bool(self.last_name and self.last_name.strip())

    def field_name(self):
        return "lastName"
