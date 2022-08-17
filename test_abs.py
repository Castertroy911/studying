import time
import math
from conftest import *


@pytest.mark.parametrize('lnk', ["895", "896", "897", "898", "899", "903", "904", "905"])
class TestCorrect:
    def test_see_correct_answer(self, browser, lnk):
        answer = math.log(int(time.time()))
        browser.implicitly_wait(15)

        link = f"https://stepik.org/lesson/236{lnk}/step/1"
        browser.get(link)

        text = browser.find_element(By.CLASS_NAME, "ember-text-area")
        text.send_keys(answer)

        button = browser.find_element(By.CLASS_NAME, "submit-submission")
        button.click()

        feedback = browser.find_element(By.CLASS_NAME, "smart-hints__hint")

        assert feedback.text == "Correct!", feedback.text
