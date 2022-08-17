from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
class TestAbs(unittest.TestCase):
 def test_register1(self):
      browser.get("http://suninjuly.github.io/registration1.html")
      first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your first name']")
      first_name.send_keys("Test")

      second_name = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your last name']")
      second_name.send_keys("Testovich")

      mail = browser.find_element(By.CLASS_NAME, "third")
      mail.send_keys("test@gmail.com")

      button = browser.find_element(By.CLASS_NAME, "btn")
      button.click()

      congratulation = browser.find_element(By.TAG_NAME, "h1").text

      self.assertEqual(congratulation, "Congratulations! You have successfully registered!", "Test failed")

 def test_register2(self):
  try:
      browser.get("http://suninjuly.github.io/registration2.html")
      first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your first name']")
      first_name.send_keys("Test")

      second_name = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your last name']")
      second_name.send_keys("Testovich")

      mail = browser.find_element(By.CLASS_NAME, "third")
      mail.send_keys("test@gmail.com")

      button = browser.find_element(By.CLASS_NAME, "btn")
      button.click()

      congratulation = browser.find_element(By.TAG_NAME, "h1").text

      self.assertEqual(congratulation, "Congratulations! You have successfully registered!", "Test failed")
  finally:
       time.sleep(10)
       browser.quit()

if __name__ == "__main__":
 unittest.main()