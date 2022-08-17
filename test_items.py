from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class TestItems:
    def test_add_to_card_button(self, browser):
        try:
            browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
            button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket1")
        except NoSuchElementException as err:
            assert err is None, "Add to basket button isn't here :)"
