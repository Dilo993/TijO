class Order:
    def __init__(self, id, items, customer):
        self.id = id
        self.items = items
        self.customer = customer



class ValidateOrder:
    def _validate_order(self, order):
        print("Walidacja zamowienia.")

class SaveOrder:
    def _save_order_to_database(self, order):
        print("Zapisywanie zamowienia do bazy danych.")

class sendConfirmationEmail:
    def _send_confirmation_email(self, order):
        print("Wysylanie e-maila potwierdzajacego.")

class OrderProcessor:
    def __init__(self, order, validator, saver, email_sender):
        self.order = order
        self.validator = validator
        self.saver = saver
        self.email_sender = email_sender

    def process_order(self):
        self.validator._validate_order(self.order)
        self.saver._save_order_to_database(self.order)
        self.email_sender._send_confirmation_email(self.order)


order = Order("123", ["Produkt A", "Produkt B"], "Jan Kowalski")
validator = ValidateOrder()
saver = SaveOrder()
email_sender = sendConfirmationEmail()
processor = OrderProcessor(order, validator, saver, email_sender)
processor.process_order()