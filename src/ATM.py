class InvalidPinException(Exception):
    """
    Wyjątek zgłaszany, gdy podany PIN jest nieprawidłowy.
    """
    def __init__(self, message: str):
        super().__init__(message)

class InsufficientFundsException(Exception):
    """
    Wyjątek zgłaszany, gdy saldo jest niewystarczające do wykonania operacji.
    """
    def __init__(self, message: str):
        super().__init__(message)

class ATM:
    """
    Klasa reprezentująca bankomat (ATM) z podstawowymi operacjami bankowymi.
    """
    def __init__(self, user_pin: int, balance: float):
        self.user_pin = user_pin
        self.balance = balance

    def check_balance(self, pin: int) -> float:
        """
        Sprawdza saldo konta użytkownika.

        :param pin: PIN użytkownika.
        :return: Saldo konta użytkownika.
        :raises InvalidPinException: Jeśli podany PIN jest nieprawidłowy.
        """
        if pin != self.user_pin:
            raise InvalidPinException("Podany PIN jest nieprawidłowy.")
        return self.balance

    def deposit(self, pin: int, amount: float) -> float:
        """
        Wpłaca środki na konto użytkownika.

        :param pin: PIN użytkownika.
        :param amount: Kwota do wpłacenia.
        :return: Aktualne saldo po wpłacie.
        :raises InvalidPinException: Jeśli podany PIN jest nieprawidłowy.
        """
        if pin != self.user_pin:
            raise InvalidPinException("Podany PIN jest nieprawidłowy.")
        self.balance += amount
        return self.balance

    def withdraw(self, pin: int, amount: float) -> float:
        """
        Wypłaca środki z konta użytkownika.

        :param pin: PIN użytkownika.
        :param amount: Kwota do wypłacenia.
        :return: Aktualne saldo po wypłacie.
        :raises InsufficientFundsException: Jeśli saldo jest niewystarczające.
        :raises InvalidPinException: Jeśli podany PIN jest nieprawidłowy.
        """
        if pin != self.user_pin:
            raise InvalidPinException("Podany PIN jest nieprawidłowy.")
        if amount > self.balance:
            raise InsufficientFundsException("Niewystarczające środki na koncie.")
        self.balance -= amount
        return self.balance