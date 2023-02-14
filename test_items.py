import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    browser.implicitly_wait(2)
    # uncomment if you need to see page
    # time.sleep(30)
    add_to_basket_button = EC.visibility_of_element_located((By.CLASS_NAME, 'btn btn-lg btn-primary btn-add-to-basket'))
    assert add_to_basket_button, 'Button not found'
