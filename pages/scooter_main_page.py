from locators.scooter_main_page_locators import ScooterMainPageLocators


class ScooterMainPage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_faq_header_main_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        faq_header = self.driver.find_element(*ScooterMainPageLocators.FAQ_HEADER)
        self.driver.execute_script("arguments[0].scrollIntoView();", faq_header)

    def go_to_order_button_main_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        button = self.driver.find_element(*ScooterMainPageLocators.ORDER_BUTTON_MAIN_PAGE)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)

    def click_on_order_button_main_page(self):
        self.driver.find_element(*ScooterMainPageLocators.ORDER_BUTTON_MAIN_PAGE).click()
