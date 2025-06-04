import re

class PasswordValidator:
    def __init__(self, password):
        self.password = password

    def is_valid(self):
        if not self.password or len(self.password) < 4:
            return False
        if not re.search(r'[A-Z]', self.password):
            return False
        if not re.search(r'[a-z]', self.password):
            return False
        if not re.search(r'\d', self.password):
            return False
        if not re.search(r'[!@#$%^&*()_+\-=\[\]{};\'\\:"|,<.>/?]', self.password):
            return False
        return True

    def field_name(self):
        return "password"
