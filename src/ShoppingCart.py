import unittest

class ShoppingCart:
    def __init__(self):
        self.products = {}
        self.discount = 0

    def add_product(self, product_name: str, price: int, quantity: int) -> bool:
        if product_name in self.products:
            self.products[product_name]["quantity"] += quantity
        else:
            self.products[product_name] = {"price": price, "quantity": quantity}
        return True

    def remove_product(self, product_name: str) -> bool:
        if product_name in self.products:
            del self.products[product_name]
            return True
        return False

    def update_quantity(self, product_name: str, new_quantity: int) -> bool:
        if product_name in self.products and new_quantity > 0:
            self.products[product_name]["quantity"] = new_quantity
            return True
        elif product_name in self.products and new_quantity == 0:
            return self.remove_product(product_name)
        return False

    def get_products(self):
        return list(self.products.keys())

    def count_products(self) -> int:
        return sum(item["quantity"] for item in self.products.values())

    def get_total_price(self) -> int:
        total = sum(item["price"] * item["quantity"] for item in self.products.values())
        return total - (total * self.discount // 100)

    def apply_discount_code(self, discount_code: str) -> bool:
        discounts = {"DISCOUNT10": 10, "DISCOUNT20": 20}
        if discount_code in discounts:
            self.discount = discounts[discount_code]
            return True
        return False

    def checkout(self) -> bool:
        if self.products:
            self.products.clear()
            self.discount = 0
            return True
        return False

