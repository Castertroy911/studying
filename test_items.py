from selenium.webdriver.common.by import By
class TestItems:
    def test_add_to_card_button(self, browser):
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        assert button, "Add to basket button isn't here :)"
