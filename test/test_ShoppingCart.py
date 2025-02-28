import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from ShoppingCart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_product(self):
        self.assertTrue(self.cart.add_product("produkt", 3000, 1))
        self.assertIn("produkt", self.cart.get_products())
    
    def test_remove_product(self):
        self.cart.add_product("produkt", 3000, 1)
        self.assertTrue(self.cart.remove_product("produkt"))
        self.assertNotIn("produkt", self.cart.get_products())
    
    def test_update_quantity(self):
        self.cart.add_product("produkt", 3000, 1)
        self.assertTrue(self.cart.update_quantity("produkt", 2))
        self.assertEqual(self.cart.count_products(), 2)
    
    def test_get_products(self):
        self.cart.add_product("produkt", 3000, 1)
        self.cart.add_product("produkt2", 100, 2)
        self.assertEqual(sorted(self.cart.get_products()), ["produkt", "produkt2"])
    
    def test_count_products(self):
        self.cart.add_product("produkt", 3000, 1)
        self.cart.add_product("produkt2", 100, 2)
        self.assertEqual(self.cart.count_products(), 3)
    
    def test_get_total_price(self):
        self.cart.add_product("produkt", 3000, 1)
        self.cart.add_product("produkt2", 100, 2)
        self.assertEqual(self.cart.get_total_price(), 3200)
    
    def test_apply_discount_code(self):
        self.cart.add_product("produkt", 3000, 1)
        self.assertTrue(self.cart.apply_discount_code("DISCOUNT10"))
        self.assertEqual(self.cart.get_total_price(), 2700)
    
    def test_checkout(self):
        self.cart.add_product("produkt", 3000, 1)
        self.assertTrue(self.cart.checkout())
        self.assertEqual(self.cart.count_products(), 0)

if __name__ == "__main__":
    unittest.main()
