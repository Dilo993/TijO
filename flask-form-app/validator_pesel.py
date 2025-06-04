class PeselValidator:
    def __init__(self, pesel):
        self.pesel = pesel

    def is_valid(self):
        if not self.pesel or len(self.pesel) != 11 or not self.pesel.isdigit():
            return False
        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
        checksum = sum(int(self.pesel[i]) * weights[i] for i in range(10))
        control_digit = (10 - (checksum % 10)) % 10
        return control_digit == int(self.pesel[10])

    def field_name(self):
        return "pesel"
