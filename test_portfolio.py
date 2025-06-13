import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PORTFOLIO_URL = "https://tgadek.bitbucket.io/app/portfolio/dev/index.html"

class TestPortfolio(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_not_email(self):
        self.driver.get(PORTFOLIO_URL)
        email = self.driver.find_element(By.ID, "email")
        email.send_keys("23")
        self.driver.find_element(By.TYPE, "submit").click()
        time.sleep(1)
        error = self.driver.find_element(By.CLASS_NAME, "error-message")
        self.assertTrue(error.is_displayed())
        self.assertIn("email", error.text.lower())

    def test_invalid_email_format(self):
        self.driver.get(PORTFOLIO_URL)
        email = self.driver.find_element(By.ID, "email")
        email.send_keys("2@2")
        self.driver.find_element(By.TYPE, "submit").click()
        time.sleep(1)
        error = self.driver.find_element(By.CLASS_NAME, "error-message")
        self.assertTrue(error.is_displayed())
        self.assertIn("email", error.text.lower())

    def test_valid_email_format(self):
        self.driver.get(PORTFOLIO_URL)
        email = self.driver.find_element(By.ID, "email")
        email.send_keys("2@2.com")
        self.driver.find_element(By.TYPE, "submit").click()
        time.sleep(1)
        errors = self.driver.find_elements(By.CLASS_NAME, "error-message")
        if errors:
            self.assertFalse(any(e.is_displayed() and "email" in e.text.lower() for e in errors))

if __name__ == '__main__':
    unittest.main()
