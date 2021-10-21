from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math
import os
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.implicitly_wait(5)
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser.get(link)
    cond = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.ID, "book")
    button.click()

    #
    # button = browser.find_element_by_css_selector(".trollface.btn")
    # button.click()
    #
    # new_wind = browser.window_handles[1]
    # browser.switch_to.window(new_wind)
    #
    x = browser.find_element(By.ID, "input_value").text
    x = int(x)
    y = calc(x)
    y = str(y)
    #
    send = browser.find_element_by_css_selector(".form-control")
    send.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()
finally:
    time.sleep(10)
    browser.quit()