import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

CALCULATOR_URL = "https://tgadek.bitbucket.io/app/calc/dev/index.html"

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """
        Inicjalizacja testu - uruchomienie przeglądarki Edge i otwarcie strony kalkulatora
        """
        self.service = Service(EdgeChromiumDriverManager().install())
        self.driver = webdriver.Edge(service=self.service)
        self.driver.get(CALCULATOR_URL)

    def test_addition(self):
        """
        Test sprawdzający działanie operacji dodawania w kalkulatorze
        """
        number1 = self.driver.find_element(By.ID, "number1")
        number1.send_keys("1")
        number2 = self.driver.find_element(By.ID, "number2")
        number2.send_keys("2")

        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()

        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, "3")

    def test_large_numbers(self):
        """
        Test sprawdzający dodawanie dużych liczb
        """
        number1 = self.driver.find_element(By.ID, "number1")
        number1.send_keys("999999999")
        number2 = self.driver.find_element(By.ID, "number2")
        number2.send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, "1000000000")

    def test_floats(self):
        """
        Test sprawdzający dodawanie liczb ułamkowych
        """
        number1 = self.driver.find_element(By.ID, "number1")
        number1.send_keys("0.5")
        number2 = self.driver.find_element(By.ID, "number2")
        number2.send_keys("0.5")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, "1")

    def tearDown(self):
        """
        Zakończenie testu - zamknięcie przeglądarki
        """
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
