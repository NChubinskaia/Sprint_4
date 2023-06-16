from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, element):
        element.click()

    def wait_for_load(self, element):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(element))
